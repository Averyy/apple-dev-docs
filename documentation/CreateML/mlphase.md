# MLPhase

**Framework**: Create ML  
**Kind**: enum

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
- [MLPhase.initialized](mlphase/initialized.md)
  The training session is in the initial idle state before extracting features and training.
- [MLPhase.extractingFeatures](mlphase/extractingfeatures.md)
  The training session is extracting features from the training dataset.
- [MLPhase.training](mlphase/training.md)
  The training session is training a model from the features it extracted from the training dataset.
- [MLPhase.evaluating](mlphase/evaluating.md)
  The training session is evaluating the model it trained.
- [MLPhase.inferencing](mlphase/inferencing.md)
  The training session is using the model to make a prediction.
### Creating a phase from a string
- [init?(rawValue: String)](mlphase/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Getting a phase’s string value
- [var rawValue: String](mlphase/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [typealias RawValue](mlphase/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Encoding and decoding a phase
- [func encode(to: any Encoder) throws](mlphase/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [init(from: any Decoder) throws](mlphase/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.
### Providing a phase’s hash value
- [func hash(into: inout Hasher)](mlphase/hash(into:).md)
- [var hashValue: Int](mlphase/hashvalue.md)
### Comparing phases
- [static func != (Self, Self) -> Bool](mlphase/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mlphase/equatable-implementations.md)
- [RawRepresentable Implementations](mlphase/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var phase: MLPhase](mltrainingsession/phase.md)
  The training session’s current state.
- [var iteration: Int](mltrainingsession/iteration.md)
  The iteration number of a training session’s phase.
- [var checkpoints: [MLCheckpoint]](mltrainingsession/checkpoints.md)
  An array of checkpoints the training session has created so far.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlphase)*