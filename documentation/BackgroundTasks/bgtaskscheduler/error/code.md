# BGTaskScheduler.Error.Code

**Framework**: Background Tasks  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the task scheduling errors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum BGTaskSchedulerErrorCode : NSInteger;
```

## Topics

### Identifying an error
- [BGTaskScheduler.Error.Code.notPermitted](./code/notpermitted.md)
  A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskScheduler.Error.Code.tooManyPendingTaskRequests](./code/toomanypendingtaskrequests.md)
  A task scheduling error that indicates there are too many pending tasks of the type requested.
- [BGTaskScheduler.Error.Code.unavailable](./code/unavailable.md)
  A task scheduling error that indicates the app or extension can’t schedule background work.
- [BGTaskScheduler.Error.Code.immediateRunIneligible](./code/immediaterunineligible.md)
  A task scheduling error that indicates a task request didn’t run immediately due to system conditions.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Handling errors
- [BGTaskScheduler.Error](../error.md)
  The Errors for the `BGTaskSchedulerError` domain.
- [class let errorDomain: String](../errordomain.md)
  The background tasks error domain as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code)*