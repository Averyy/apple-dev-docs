# BGTask

**Framework**: Background Tasks  
**Kind**: class  
**Role**: Class

An abstract class for the framework’s tasks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGTask
```

```objc
@interface BGTask : NSObject
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](./performing-long-running-tasks-on-ios-and-ipados.md)

#### Overview

With the exception of [`BGContinuedProcessingTask`](./bgcontinuedprocessingtask.md), which your app executes in the foreground, the system executes [`BGTask`](./bgtask.md) subclasses on behalf of your app, while your app is in the background.

## Topics

### Reading Task Information
- [var identifier: String](./bgtask/identifier.md)
  The string identifier of the task.
### Configuring a Task
- [var expirationHandler: (() -> Void)?](./bgtask/expirationhandler.md)
  A handler called shortly before the task’s background time expires.
- [func setTaskCompleted(success: Bool)](./bgtask/settaskcompleted%28success%29.md)
  Informs the background task scheduler that the task is complete.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [BGAppRefreshTask](./bgapprefreshtask.md)
- [BGContinuedProcessingTask](./bgcontinuedprocessingtask.md)
- [BGProcessingTask](./bgprocessingtask.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Background Tasks updates](../Updates/backgroundtasks.md)
  Learn about important changes in Background Tasks.
- [class BGTaskScheduler](./bgtaskscheduler.md)
  A class for scheduling tasks that add background support to your app’s most critical work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtask)*