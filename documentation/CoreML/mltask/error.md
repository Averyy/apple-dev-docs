# error

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The underlying error if the task is in a failed state.

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
var error: (any Error)? { get }
```

```objc
@property (atomic, copy, readonly, nullable) NSError * error;
```

## See Also

### Checking the state of a task
- [var state: MLTaskState](./state.md)
  The current state of the machine learning task.
- [enum MLTaskState](../mltaskstate.md)
  The state of a machine learning task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltask/error)*