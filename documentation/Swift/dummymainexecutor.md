# DummyMainExecutor

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
final class DummyMainExecutor
```

## Topics

### Initializers
- [init()](dummymainexecutor/init.md)
### Instance Properties
- [var isMainExecutor: Bool](dummymainexecutor/ismainexecutor.md)
  `true` if this is the main executor.
### Instance Methods
- [func checkIsolated()](dummymainexecutor/checkisolated.md)
  Last resort “fallback” isolation check, called when the concurrency runtime is comparing executors e.g. during `assumeIsolated()` and is unable to prove serial equivalence between the expected (this object), and the current executor.
- [func enqueue(consuming ExecutorJob)](dummymainexecutor/enqueue(_:).md)
- [func run() throws](dummymainexecutor/run.md)
  Run the executor’s run loop.
- [func stop()](dummymainexecutor/stop.md)
  Signal to the run loop to stop running and return.
### Default Implementations
- [RunLoopExecutor Implementations](dummymainexecutor/runloopexecutor-implementations.md)
- [SerialExecutor Implementations](dummymainexecutor/serialexecutor-implementations.md)

## Relationships

### Conforms To
- [Executor](executor.md)
- [MainExecutor](mainexecutor.md)
- [RunLoopExecutor](runloopexecutor.md)
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
- [class CFMainExecutor](cfmainexecutor.md)
- [class CFTaskExecutor](cftaskexecutor.md)
- [class DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [class DispatchMainExecutor](dispatchmainexecutor.md)
- [class DummyTaskExecutor](dummytaskexecutor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dummymainexecutor)*