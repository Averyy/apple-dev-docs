# SchedulableExecutor

**Framework**: Swift  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol SchedulableExecutor : Executor
```

## Topics

### Instance Methods
- [func enqueue<C>(consuming ExecutorJob, after: C.Duration, tolerance: C.Duration?, clock: C)](schedulableexecutor/enqueue(_:after:tolerance:clock:).md)
  Enqueue a job to run after a specified delay.
- [func enqueue<C>(consuming ExecutorJob, at: C.Instant, tolerance: C.Duration?, clock: C)](schedulableexecutor/enqueue(_:at:tolerance:clock:).md)
  Enqueue a job to run at a specified time.

## Relationships

### Inherits From
- [Executor](executor.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
### Conforming Types
- [CFMainExecutor](cfmainexecutor.md)
- [CFTaskExecutor](cftaskexecutor.md)
- [DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [DispatchMainExecutor](dispatchmainexecutor.md)

## See Also

- [protocol MainExecutor](mainexecutor.md)
  The main executor must conform to these three protocols; we have to make this a protocol for compatibility with Embedded Swift.
- [protocol RunLoopExecutor](runloopexecutor.md)
  An executor that is backed by some kind of run loop.
- [protocol ExecutorFactory](executorfactory.md)
  An ExecutorFactory is used to create the default main and task executors.
- [struct PlatformExecutorFactory](platformexecutorfactory.md)
- [class CFMainExecutor](cfmainexecutor.md)
- [class CFTaskExecutor](cftaskexecutor.md)
- [class DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [class DispatchMainExecutor](dispatchmainexecutor.md)
- [class DummyMainExecutor](dummymainexecutor.md)
- [class DummyTaskExecutor](dummytaskexecutor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/schedulableexecutor)*