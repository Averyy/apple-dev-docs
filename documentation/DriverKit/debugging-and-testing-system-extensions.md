# Debugging and testing system extensions

**Framework**: DriverKit

Debug your system extensions by temporarily disabling the security checks that macOS performs during the installation process.

#### Overview

When you activate a system extension from your app, the system requires your extension to have the proper entitlements and code signature. It must also meet all other criteria for running on the user’s system. If the extension doesn’t meet all of the requirements, the activation request fails with an error. During the development of a system extension, you can disable some validation checks to simplify writing and testing your code.

> ❗ **Important**:  Always remember to reenable all validation checks and perform additional testing before shipping your system extension to users. Disabling validation checks is only appropriate during the development process on your local system.

##### Enable Activation From Any Directory

You must place all system extensions in the `Contents/Library/SystemExtensions` directory of your app bundle, and the app itself must be installed in one of the system’s `Applications` directories. To allow development of your app outside of these directories, use the `systemextensionsctl` command-line tool to enable developer mode. When in developer mode, the system doesn’t check the location of your system extension prior to loading it, so you can load it from anywhere in the file system. To enable developer mode, open a Terminal window and execute the following command:

`% systemextensionsctl developer on`

To turn developer mode off, open Terminal and run the same tool with `developer off` as the parameter.

##### Disable Code Signing and Notarization Checks

System Integrity Protection (SIP) in macOS prevents unauthorized code from running on your system. Xcode doesn’t notarize apps or system extensions during the normal development cycle, so disabling SIP bypasses the notarization checks that the system normally performs, and allows you to debug your code more quickly.

For information on how to disable SIP, see [`Disabling and Enabling System Integrity Protection`](https://developer.apple.com/documentation/Security/disabling-and-enabling-system-integrity-protection).

##### Attach the Debugger to Your System Extension

Because the system loads system extensions dynamically, attach the debugger to your system extension’s process after the system launches it. The `lldb` command-line tool provides a way to attach to any process and examine its state. To use this tool for your system extension, do the following:

1. After your system extension launches, run the `ps` command-line tool and note your extension’s process ID.
2. Run `lldb` from Terminal as the superuser.
3. Attach to the process using the `process attach --pid` command in `lldb`.

After you attach to your system extension’s process, you can use `lldb` to examine its threads and other state information. To view a list of commands available from the `lldb` command-line tool, run the tool in Terminal and type `help`.

##### Test Your Driver Extensions on Arm64e

Driver extensions (dexts) often coordinate with kernel extensions (kexts) to perform certain tasks. On Apple silicon, kexts use the `arm64e` architecture, which includes support for pointer authentication codes (PACs). During your testing cycle, try to build your dext for the `arm64e` architecture and address any issues that arise. To test your dext, do the following:

1. Reboot your Mac with Apple silicon into Recovery mode.
2. Set the security level to Medium.
3. Disable System Integrity Protection, as descrbed in [`Disabling and Enabling System Integrity Protection`](https://developer.apple.com/documentation/Security/disabling-and-enabling-system-integrity-protection).
4. Reboot back to macOS.
5. Add the `-arm64e_preview_abi` boot arg to your system.

The following example shows you how to use the `nvram` command-line tool to add the `-arm64e_preview_abi` boot arg:

```sh
sudo nvram boot-args=-arm64e_preview_abi
```

## See Also

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)
  Create a driver that supports proprietary features of your company’s hardware devices.
- [IOService](ioservice.md)
  The base class for managing the setup and registration of your driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/debugging-and-testing-system-extensions)*