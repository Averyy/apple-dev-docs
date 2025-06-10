# CFMainExecutor

**Framework**: Swift  
**Kind**: class

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
final class CFMainExecutor
```

## Topics

### Initializers
- [init()](cfmainexecutor/init.md)
### Instance Methods
- [func run() throws](cfmainexecutor/run.md)
  Run the executor’s run loop.
- [func stop()](cfmainexecutor/stop.md)
  Signal to the run loop to stop running and return.

## Relationships

### Inherits From
- [DispatchMainExecutor](dispatchmainexecutor.md)
### Conforms To
- [Executor](executor.md)
- [MainExecutor](mainexecutor.md)
- [RunLoopExecutor](runloopexecutor.md)
- [SchedulableExecutor](schedulableexecutor.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [SerialExecutor](serialexecutor.md)

## See Also

- [protocol MainExecutor](mainexecutor.md)
  The main executor must conform to these three protocols; we have to make this a protocol for compatibility with Embedded Swift.
- [protocol RunLoopExecutor](runloopexecutor.md)
  An executor that is backed by some kind of run loop.
- [protocol SchedulableExecutor](schedulableexecutor.md)
- [protocol ExecutorFactory](executorfactory.md)
  An ExecutorFactory is used to create the default main and task executors.
- [struct PlatformExecutorFactory](platformexecutorfactory.md)
- [class CFTaskExecutor](cftaskexecutor.md)
- [class DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [class DispatchMainExecutor](dispatchmainexecutor.md)
- [class DummyMainExecutor](dummymainexecutor.md)
- [class DummyTaskExecutor](dummytaskexecutor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/cfmainexecutor)*