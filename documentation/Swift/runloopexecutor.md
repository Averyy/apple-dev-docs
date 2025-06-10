# RunLoopExecutor

**Framework**: Swift  
**Kind**: protocol

An executor that is backed by some kind of run loop.

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
protocol RunLoopExecutor : Executor
```

#### Overview

The idea here is that some executors may work by running a loop that processes events of some sort; we want a way to enter that loop, and we would also like a way to trigger the loop to exit.

## Topics

### Instance Methods
- [func run() throws](runloopexecutor/run.md)
  Run the executor’s run loop.
- [func runUntil(() -> Bool) throws](runloopexecutor/rununtil(_:).md)
  Run the executor’s run loop until a condition is satisfied.
- [func stop()](runloopexecutor/stop.md)
  Signal to the run loop to stop running and return.

## Relationships

### Inherits From
- [Executor](executor.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
### Inherited By
- [MainExecutor](mainexecutor.md)
### Conforming Types
- [CFMainExecutor](cfmainexecutor.md)
- [DispatchMainExecutor](dispatchmainexecutor.md)
- [DummyMainExecutor](dummymainexecutor.md)

## See Also

- [protocol MainExecutor](mainexecutor.md)
  The main executor must conform to these three protocols; we have to make this a protocol for compatibility with Embedded Swift.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/runloopexecutor)*