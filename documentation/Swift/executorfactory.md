# ExecutorFactory

**Framework**: Swift  
**Kind**: protocol

An ExecutorFactory is used to create the default main and task executors.

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
protocol ExecutorFactory
```

## Topics

### Type Properties
- [static var defaultExecutor: any TaskExecutor](executorfactory/defaultexecutor.md)
  Constructs and returns the default or global executor, which is the default place in which we run tasks.
- [static var mainExecutor: any MainExecutor](executorfactory/mainexecutor.md)
  Constructs and returns the main executor, which is started implicitly by the `async main` entry point and owns the “main” thread.

## Relationships

### Conforming Types
- [PlatformExecutorFactory](platformexecutorfactory.md)

## See Also

- [protocol MainExecutor](mainexecutor.md)
  The main executor must conform to these three protocols; we have to make this a protocol for compatibility with Embedded Swift.
- [protocol RunLoopExecutor](runloopexecutor.md)
  An executor that is backed by some kind of run loop.
- [protocol SchedulableExecutor](schedulableexecutor.md)
- [struct PlatformExecutorFactory](platformexecutorfactory.md)
- [class CFMainExecutor](cfmainexecutor.md)
- [class CFTaskExecutor](cftaskexecutor.md)
- [class DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [class DispatchMainExecutor](dispatchmainexecutor.md)
- [class DummyMainExecutor](dummymainexecutor.md)
- [class DummyTaskExecutor](dummytaskexecutor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorfactory)*