# MLPhase

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The possible states of a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MLPhase
```

## Topics

### Retrieving session phases
- [MLPhase.initialized](./mlphase/initialized.md)
  The training session is in the initial idle state before extracting features and training.
- [MLPhase.extractingFeatures](./mlphase/extractingfeatures.md)
  The training session is extracting features from the training dataset.
- [MLPhase.training](./mlphase/training.md)
  The training session is training a model from the features it extracted from the training dataset.
- [MLPhase.evaluating](./mlphase/evaluating.md)
  The training session is evaluating the model it trained.
- [MLPhase.inferencing](./mlphase/inferencing.md)
  The training session is using the model to make a prediction.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking a training session’s progress
- [var phase: MLPhase](./mltrainingsession/phase.md)
  The training session’s current state.
- [var iteration: Int](./mltrainingsession/iteration.md)
  The iteration number of a training session’s phase.
- [var checkpoints: [MLCheckpoint]](./mltrainingsession/checkpoints.md)
  An array of checkpoints the training session has created so far.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlphase)*