# NSUserAutomatorTask

**Framework**: Foundation  
**Kind**: class

An object that executes Automator workflows.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSUserAutomatorTask
```

#### Overview

The [`NSUserAutomatorTask`](nsuserautomatortask.md) class is intended to run Automator workflows from your application. It is intended to execute user-supplied workflows, and will execute them outside of the application’s sandbox, if any.

The class is not intended to execute scripts built into an application; for that, use one of the [`Process`](process.md) or [`AMWorkflow`](https://developer.apple.com/documentation/Automator/AMWorkflow) classes.  If the application is sandboxed, then the script must be in the [`FileManager.SearchPathDirectory.applicationScriptsDirectory`](filemanager/searchpathdirectory/applicationscriptsdirectory.md) folder.  A sandboxed application may read from, but not write to, this folder.

If you simply need to execute scripts without regard to input or output, use [`NSUserScriptTask`](nsuserscripttask.md), which can execute any of the specific types.  If you need specific control over the input to or output from the workflow, use this class.

## Topics

### Executing Automator Tasks
- [func execute(withInput: (any NSSecureCoding)?, completionHandler: NSUserAutomatorTask.CompletionHandler?)](nsuserautomatortask/execute(withinput:completionhandler:).md)
  Execute the Automator workflow by providing it as securely coded input.
- [var variables: [String : Any]?](nsuserautomatortask/variables.md)
  The variables required by the Automator workflow.
### Constants
- [NSUserAutomatorTask.CompletionHandler](nsuserautomatortask/completionhandler.md)
  Implement this block to retrieve the output of the Automator workflow executed by [`execute(withInput:completionHandler:)`](nsuserautomatortask/execute(withinput:completionhandler:).md).

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
- [class NSUserUnixTask](nsuserunixtask.md)
  An object that executes unix applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserautomatortask)*