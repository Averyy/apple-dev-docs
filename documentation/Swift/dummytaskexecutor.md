# DummyTaskExecutor

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
final class DummyTaskExecutor
```

## Topics

### Initializers
- [init()](dummytaskexecutor/init.md)
### Instance Properties
- [var isMainExecutor: Bool](dummytaskexecutor/ismainexecutor.md)
  `true` if this is the main executor.
### Instance Methods
- [func enqueue(consuming ExecutorJob)](dummytaskexecutor/enqueue(_:).md)
### Default Implementations
- [TaskExecutor Implementations](dummytaskexecutor/taskexecutor-implementations.md)

## Relationships

### Conforms To
- [Executor](executor.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [TaskExecutor](taskexecutor.md)

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
- [class DummyMainExecutor](dummymainexecutor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dummytaskexecutor)*