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
### Instance Properties
- [var cancellationHandler: (() -> (any Error)?)?](fstask/cancellationhandler.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class FSTaskOptions](fstaskoptions.md)
  A class that passes command options to a task, optionally providing security-scoped URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask)*