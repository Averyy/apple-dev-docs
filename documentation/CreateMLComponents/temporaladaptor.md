# TemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A temporal transformer that applies a regular transformer to each value of a temporal sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TemporalAdaptor<Base> where Base : Transformer, Base : Sendable
```

## Topics

### Initializers
- [init(Base)](temporaladaptor/init(_:).md)
  Creates a temporal transformer from a transformer.
### Instance Methods
- [func applied(to: some TemporalSequence<Base.Input>, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<TemporalAdaptor<Base>.Output>](temporaladaptor/applied(to:eventhandler:).md)
  Performs the transformation on each element of the input sequence.
### Type Aliases
- [TemporalAdaptor.Input](temporaladaptor/input.md)
  The input type.
- [TemporalAdaptor.Output](temporaladaptor/output.md)
  The output type.
- [TemporalAdaptor.OutputSequence](temporaladaptor/outputsequence.md)
  The output sequence type.
### Default Implementations
- [TemporalTransformer Implementations](temporaladaptor/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [TemporalTransformer](temporaltransformer.md)

## See Also

- [struct TemporalTransformerToEstimatorAdaptor](temporaltransformertoestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
- [struct TemporalEstimatorToSupervisedAdaptor](temporalestimatortosupervisedadaptor.md)
  An adaptor that exposes a temporal estimator as a supervised temporal estimator.
- [struct TemporalTransformerToUpdatableEstimatorAdaptor](temporaltransformertoupdatableestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaladaptor)*