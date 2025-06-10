# MLTaskState

**Framework**: Core ML  
**Kind**: enum

The state of a machine learning task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum MLTaskState
```

## Topics

### Transient States
- [MLTaskState.running](mltaskstate/running.md)
  The state of a machine learning task that’s executing.
- [MLTaskState.suspended](mltaskstate/suspended.md)
  The state of a machine learning task that’s paused.
- [MLTaskState.cancelling](mltaskstate/cancelling.md)
  The state of a machine learning task that’s in mid-termination, before it could finish successfully.
### Final States
- [MLTaskState.completed](mltaskstate/completed.md)
  The state of a machine learning task that has finished successfully.
- [MLTaskState.failed](mltaskstate/failed.md)
  The state of a machine learning task that has terminated due to an error.
### Initializers
- [init?(rawValue: Int)](mltaskstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: MLTaskState](mltask/state.md)
  The current state of the machine learning task.
- [var error: (any Error)?](mltask/error.md)
  The underlying error if the task is in a failed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltaskstate)*