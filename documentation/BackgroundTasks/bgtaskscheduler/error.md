# BGTaskScheduler.Error

**Framework**: Background Tasks  
**Kind**: struct  
**Role**: Structure

The Errors for the `BGTaskSchedulerError` domain.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Error
```

## Topics

### Getting the error codes
- [BGTaskScheduler.Error.Code](./error/code.md)
  An enumeration of the task scheduling errors.
- [static var notPermitted: BGTaskScheduler.Error.Code](./error/notpermitted.md)
  A task scheduling error that indicates the app isn’t permitted to launch the task.
- [static var tooManyPendingTaskRequests: BGTaskScheduler.Error.Code](./error/toomanypendingtaskrequests.md)
  A task scheduling error that indicates there are too many pending tasks of the type requested.
- [static var unavailable: BGTaskScheduler.Error.Code](./error/unavailable.md)
  A task scheduling error that indicates the app or extension can’t schedule background work.
### Getting the error domain
- [static var errorDomain: String](./error/errordomain.md)
  The background tasks error domain as a string.
### Type Properties
- [static var immediateRunIneligible: BGTaskScheduler.Error.Code](./error/immediaterunineligible.md)

## Relationships

### Conforms To
- [CustomNSError](../../Foundation/customnserror.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling errors
- [BGTaskScheduler.Error.Code](./error/code.md)
  An enumeration of the task scheduling errors.
- [class let errorDomain: String](./errordomain.md)
  The background tasks error domain as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error)*