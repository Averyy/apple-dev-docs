# NSUserAppleScriptTask

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that executes AppleScript scripts.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSUserAppleScriptTask
```

```objc
@interface NSUserAppleScriptTask : NSUserScriptTask
```

## Overview

The [`NSUserAppleScriptTask`](./nsuserapplescripttask.md) class is intended to run AppleScript scripts from your application. It is intended to execute user-supplied scripts and will execute them outside of the application’s sandbox, if any.

The class is not intended to execute scripts built into an application; for that, use one of the [`Process`](./process.md) classes. If the application is sandboxed, then the script must be in the [`FileManager.SearchPathDirectory.applicationScriptsDirectory`](./filemanager/searchpathdirectory/applicationscriptsdirectory.md) folder. A sandboxed application may read from, but not write to, this folder.

If you simply need to execute scripts without regard to input or output, use [`NSUserScriptTask`](./nsuserscripttask.md), which can execute any of the specific types. If you need specific control over the input to or output from the script, use this class.

## Topics

### Executing an AppleScript Script
- [func execute(withAppleEvent: NSAppleEventDescriptor?, completionHandler: NSUserAppleScriptTask.CompletionHandler?)](./nsuserapplescripttask/execute%28withappleevent,completionhandler%29.md)
  Execute the AppleScript script by sending it the specified Apple event.
### Constants
- [NSUserAppleScriptTask.CompletionHandler](./nsuserapplescripttask/completionhandler.md)
  Implement this block to retrieve the result of the AppleScript executed by [`execute(withAppleEvent:completionHandler:)`](./nsuserapplescripttask/execute%28withappleevent,completionhandler%29.md).

## Relationships

### Inherits From
- [NSUserScriptTask](./nsuserscripttask.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scripts and External Tasks
- [class Process](./process.md)
  An object that represents a subprocess of the current process.
- [class NSUserScriptTask](./nsuserscripttask.md)
  An object that executes scripts.
- [class NSUserAutomatorTask](./nsuserautomatortask.md)
  An object that executes Automator workflows.
- [class NSUserUnixTask](./nsuserunixtask.md)
  An object that executes unix applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserapplescripttask)*