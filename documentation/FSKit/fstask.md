# FSTask

**Framework**: FSKit  
**Kind**: class

A class that enables a file system module to pass log messages and completion notifications to clients.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSTask
```

#### Overview

FSKit creates an instance of this class for each long-running operations.

## Topics

### Logging
- [func logMessage(String)](fstask/logmessage(_:).md)
  Logs the given string to the initiating client.
### Sending completion messages
- [func didComplete(error: (any Error)?)](fstask/didcomplete(error:).md)
  Informs the client that the task completed.
### Handling task cancellation
- [var cancellationHandler: (() -> (any Error)?)?](fstask/cancellationhandler.md)
  A handler called by FSKit upon canceling the task.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class FSTaskOptions](fstaskoptions.md)
  A class that passes command options to a task, optionally providing security-scoped URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask)*