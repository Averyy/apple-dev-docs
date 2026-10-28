# FSTask

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A class that enables a file system module to pass log messages and completion notifications to clients.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSTask
```

```objc
@interface FSTask : NSObject
```

## Overview

FSKit creates an instance of this class for each long-running operations.

## Topics

### Logging
- [func logMessage(String)](./fstask/logmessage%28_%29.md)
  Logs the given string to the initiating client.
### Sending completion messages
- [func didComplete(error: (any Error)?)](./fstask/didcomplete%28error%29.md)
  Informs the client that the task completed.
### Handling task cancellation
- [var cancellationHandler: (() -> (any Error)?)?](./fstask/cancellationhandler.md)
  A handler called by FSKit upon canceling the task.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Tasks
- [class FSTaskOptions](./fstaskoptions.md)
  A class that passes command options to a task, optionally providing security-scoped URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask)*