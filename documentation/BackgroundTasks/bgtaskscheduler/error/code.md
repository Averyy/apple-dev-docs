# BGTaskScheduler.Error.Code

**Framework**: Background Tasks  
**Kind**: enum

An enumeration of the task scheduling errors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum Code
```

## Topics

### Identifying an error
- [BGTaskScheduler.Error.Code.notPermitted](bgtaskscheduler/error/code/notpermitted.md)
  A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskScheduler.Error.Code.tooManyPendingTaskRequests](bgtaskscheduler/error/code/toomanypendingtaskrequests.md)
  A task scheduling error that indicates there are too many pending tasks of the type requested.
- [BGTaskScheduler.Error.Code.unavailable](bgtaskscheduler/error/code/unavailable.md)
  A task scheduling error that indicates the app or extension can’t schedule background work.
- [BGTaskScheduler.Error.Code.immediateRunIneligible](bgtaskscheduler/error/code/immediaterunineligible.md)
  A task scheduling error that indicates a task request didn’t run immediately due to system conditions.
### Initializers
- [init?(rawValue: Int)](bgtaskscheduler/error/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [BGTaskScheduler.Error](bgtaskscheduler/error.md)
  The Errors for the `BGTaskSchedulerError` domain.
- [class let errorDomain: String](bgtaskscheduler/errordomain.md)
  The background tasks error domain as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code)*