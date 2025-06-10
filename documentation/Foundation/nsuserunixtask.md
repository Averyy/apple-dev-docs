# NSUserUnixTask

**Framework**: Foundation  
**Kind**: class

An object that executes unix applications.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSUserUnixTask
```

#### Overview

The [`NSUserUnixTask`](nsuserunixtask.md) class is intended to run unix applications, typically a shell script, from your application. It is intended to execute user-supplied scripts, and will execute them outside of the application’s sandbox, if any.

The class is not intended to execute scripts built into an application; for that, use one of the [`Process`](process.md), [`NSAppleScript`](nsapplescript.md), or [`AMWorkflow`](https://developer.apple.com/documentation/Automator/AMWorkflow) classes.  If the application is sandboxed, then the script must be in the [`FileManager.SearchPathDirectory.applicationScriptsDirectory`](filemanager/searchpathdirectory/applicationscriptsdirectory.md) folder.  A sandboxed application may read from, but not write to, this folder.

If you simply need to execute unix scripts without regard to input or output, use [`NSUserScriptTask`](nsuserscripttask.md), which can execute any of the specific types.  If you need specific control over the input to, or output from, or the error stream of the script, use this class.

## Topics

### Executing the Unix Script
- [func execute(withArguments: [String]?, completionHandler: NSUserUnixTask.CompletionHandler?)](nsuserunixtask/execute(witharguments:completionhandler:).md)
  Execute the unix script with the specified arguments.
### Standard Unix Streams
- [var standardError: FileHandle?](nsuserunixtask/standarderror.md)
  The standard error stream.
- [var standardInput: FileHandle?](nsuserunixtask/standardinput.md)
  The standard input stream.
- [var standardOutput: FileHandle?](nsuserunixtask/standardoutput.md)
  The standard output stream.
### Constants
- [NSUserUnixTask.CompletionHandler](nsuserunixtask/completionhandler.md)
  Implement this block to retrieve an error from the Unix scripted executed by [`execute(withArguments:completionHandler:)`](nsuserunixtask/execute(witharguments:completionhandler:).md).

## Relationships

### Inherits From
- [NSUserScriptTask](nsuserscripttask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class Process](process.md)
  An object that represents a subprocess of the current process.
- [class NSUserScriptTask](nsuserscripttask.md)
  An object that executes scripts.
- [class NSUserAppleScriptTask](nsuserapplescripttask.md)
  An object that executes AppleScript scripts.
- [class NSUserAutomatorTask](nsuserautomatortask.md)
  An object that executes Automator workflows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserunixtask)*