# MLPhase.evaluating

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

The training session is evaluating the model it trained.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case evaluating
```

## See Also

### Retrieving session phases
- [MLPhase.initialized](./initialized.md)
  The training session is in the initial idle state before extracting features and training.
- [MLPhase.extractingFeatures](./extractingfeatures.md)
  The training session is extracting features from the training dataset.
- [MLPhase.training](./training.md)
  The training session is training a model from the features it extracted from the training dataset.
- [MLPhase.inferencing](./inferencing.md)
  The training session is using the model to make a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlphase/evaluating)*