# Updating Mac Software

**Framework**: Security

Implement Mac software updates without causing code-signing crashes.

#### Overview

Many Mac software products include a software updater. For example:

- An app might ask the user whether they want to download and install the latest version.
- An enterprise IT department might install a daemon that updates the enterprise’s custom software each night.

If you write a software updater in the simplest way, you run the risk of a hard-to-reproduce crash in the newly updated software. The symptoms of this problem are:

- Some seemingly random part of the updated code crashes.
- The associated crash report includes the message `Code Signature Invalid`.
- The problem goes away when you restart the Mac.

> **Note**:  Apple software-update mechanisms, such as the App Store updater, the Installer app, and the `installer` command-line tool, aren’t susceptible to this code-signing crash.

##### Update Files That Include Signed Code

Imagine code that downloads an update for a command-line tool. The final step of that process might look like this:

```swift
import System
import Darwin

// Do not do this. Modifying signed code in place puts you at risk of a 
// code-signing crash.

func updateToolBadly(at executablePath: String, with newContents: [UInt8]) throws {
    let fd = try FileDescriptor.open(executablePath, .writeOnly, options: [.truncate])
    defer {
        try! fd.close()
    }
    try fd.writeAll(newContents)
}
```

This code is incorrect because it modifies the command-line tool’s executable file in place. macOS caches information about the code’s signature in the kernel. It doesn’t flush that cache when you modify the file’s contents. Modifying the file in place yields a mismatch between the file’s contents and the in-kernel cache, which can cause a hard-to-reproduce code-signing crash the next time you run the tool.

While this example uses a command-line tool to demonstrate the issue, updating any file that contains signed code might trigger this code-signing crash. That includes executables, frameworks, dynamic libraries, and bundles.

To update a file that contains signed code without risking this crash, write the updated code to a temporary file and replace the existing file with that temporary one:

```swift
func updateTool(at executablePath: String, with newContents: [UInt8], temporaryPath: String) throws {
    do {
        let permissions: FilePermissions = [[.ownerReadWriteExecute, .groupReadExecute, .otherReadExecute]]
        let fd = try FileDescriptor.open(temporaryPath, .writeOnly, options: [.create], permissions: permissions)
        defer {
            try! fd.close()
        }
        try fd.writeAll(newContents)
    }
    let success = rename(temporaryPath, executablePath) >= 0
    guard success else { throw Errno(rawValue: errno) }
}
```

Using a temporary file eliminates the risk of a code-signing crash because the in-kernel cache is associated with the old file, which remains unmodified. The new file gets its own in-kernel cache, built from the contents of that new file.

##### Check Third Party Software Updaters

If you wrote the code for your software updater, use the techniques discussed above to identify and correct this potential code-signing issue. You can also check software updater code that you didn’t write by running `ls` with the `-i` option before and after the update, to see whether the inode number changes. For example, imagine you’re installing an update using `cp` and your want to update `MyTool` with a new version, `MyTool-new`. Run the following, to test whether this exposes you to a code-signing crash:

```sh
% ls -i MyTool
78290841 MyTool
% cp MyTool-new MyTool
% ls -i MyTool  
78290841 MyTool
```

Note that the inode number didn’t change, which indicates that `cp` modified the `MyTool` file in place. This puts you at risk of a code-signing crash the next time you run `MyTool`.

Now, repeat the test, but use `ditto` in place of `cp`:

```sh
% ls -i MyTool
78290841 MyTool
% ditto MyTool-new MyTool
% ls -i MyTool  
78413900 MyTool
```

This time, the inode number changed. This change indicates that `ditto` replaced the `MyTool` file with an entirely new file, and thus avoided this potential code-signing crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/updating-mac-software)*