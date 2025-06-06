# NSUserScriptTask

**Framework**: Foundation  
**Kind**: class

An object that executes scripts.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSUserScriptTask
```

#### Overview

The [`NSUserScriptTask`](nsuserscripttask.md) class is able to run all the scripts normally run by the one of its subclasses, however it ignores the results. It is intended to execute user-supplied scripts and will execute them outside of the application’s sandbox, if any.

If you need to execute scripts and get the input and output information use the [`NSUserUnixTask`](nsuserunixtask.md), [`NSUserAppleScriptTask`](nsuserapplescripttask.md), and [`NSUserAutomatorTask`](nsuserautomatortask.md) sub classes.

## Topics

### Specifying the Script
- [init(url: URL) throws](nsuserscripttask/init(url:).md)
  Return a user script task instance given a URL for a script file.
- [var scriptURL: URL](nsuserscripttask/scripturl.md)
  The URL of the script file.
### Executing the User Script
- [func execute(completionHandler: NSUserScriptTask.CompletionHandler?)](nsuserscripttask/execute(completionhandler:).md)
  Executes the script with no input and ignoring any result.
### Constants
- [NSUserScriptTask.CompletionHandler](nsuserscripttask/completionhandler.md)
  Implement this block to retrieve the error of the script executed by [`execute(completionHandler:)`](nsuserscripttask/execute(completionhandler:).md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSUserAppleScriptTask](nsuserapplescripttask.md)
- [NSUserAutomatorTask](nsuserautomatortask.md)
- [NSUserUnixTask](nsuserunixtask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class Process](process.md)
  An object that represents a subprocess of the current process.
- [class NSUserAppleScriptTask](nsuserapplescripttask.md)
  An object that executes AppleScript scripts.
- [class NSUserAutomatorTask](nsuserautomatortask.md)
  An object that executes Automator workflows.
- [class NSUserUnixTask](nsuserunixtask.md)
  An object that executes unix applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserscripttask)*