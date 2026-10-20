# TemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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

### Creating a temporal adaptor
- [init(Base)](./temporaladaptor/init%28_%29.md)
  Creates a temporal transformer from a transformer.
### Applying a temporal adapter
- [func applied(to: some TemporalSequence<Base.Input>, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<TemporalAdaptor<Base>.Output>](./temporaladaptor/applied%28to,eventhandler%29.md)
  Performs the transformation on each element of the input sequence.
### Supporting types
- [TemporalAdaptor.Input](./temporaladaptor/input.md)
  The input type.
- [TemporalAdaptor.Output](./temporaladaptor/output.md)
  The output type.
- [TemporalAdaptor.OutputSequence](./temporaladaptor/outputsequence.md)
  The output sequence type.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TemporalTransformer](./temporaltransformer.md)

## See Also

### Temporal adaptors
- [struct TemporalTransformerToEstimatorAdaptor](./temporaltransformertoestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
- [struct TemporalEstimatorToSupervisedAdaptor](./temporalestimatortosupervisedadaptor.md)
  An adaptor that exposes a temporal estimator as a supervised temporal estimator.
- [struct TemporalTransformerToUpdatableEstimatorAdaptor](./temporaltransformertoupdatableestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaladaptor)*