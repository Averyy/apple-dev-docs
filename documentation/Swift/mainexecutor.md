# MainExecutor

**Framework**: Swift  
**Kind**: protocol

The main executor must conform to these three protocols; we have to make this a protocol for compatibility with Embedded Swift.

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
protocol MainExecutor : RunLoopExecutor, SerialExecutor
```

## Relationships

### Inherits From
- [Executor](executor.md)
- [RunLoopExecutor](runloopexecutor.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [SerialExecutor](serialexecutor.md)
### Conforming Types
- [CFMainExecutor](cfmainexecutor.md)
- [DispatchMainExecutor](dispatchmainexecutor.md)
- [DummyMainExecutor](dummymainexecutor.md)

## See Also

- [protocol RunLoopExecutor](runloopexecutor.md)
  An executor that is backed by some kind of run loop.
- [protocol SchedulableExecutor](schedulableexecutor.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mainexecutor)*