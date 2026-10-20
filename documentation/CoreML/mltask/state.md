# state

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The current state of the machine learning task.

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
var state: MLTaskState { get }
```

```objc
@property (atomic, assign, readonly) MLTaskState state;
```

## See Also

### Checking the state of a task
- [enum MLTaskState](../mltaskstate.md)
  The state of a machine learning task.
- [var error: (any Error)?](./error.md)
  The underlying error if the task is in a failed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltask/state)*