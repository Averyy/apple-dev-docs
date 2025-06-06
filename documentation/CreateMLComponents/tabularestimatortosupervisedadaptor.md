# TabularEstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An adaptor that exposes a tabular estimator as a tabular supervised estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct TabularEstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : TabularEstimator
```

## Topics

### Creating an adaptor
- [init(Estimator, annotationColumnID: ColumnID<Annotation>)](tabularestimatortosupervisedadaptor/init(_:annotationcolumnid:).md)
  Creates a tabular estimator supervised adaptor.
### Getting the properties
- [var annotationColumnID: ColumnID<Annotation>](tabularestimatortosupervisedadaptor/annotationcolumnid.md)
  The annotation column identifier.
- [let estimator: Estimator](tabularestimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(Estimator.Transformer, to: inout any EstimatorEncoder) throws](tabularestimatortosupervisedadaptor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Estimator.Transformer](tabularestimatortosupervisedadaptor/decode(from:).md)
  Decodes a previously fitted transformer.
### Fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> Estimator.Transformer](tabularestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Returns the tabular transformer fitted using the provided tabular estimator.
- [TabularEstimatorToSupervisedAdaptor.Transformer](tabularestimatortosupervisedadaptor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTabularEstimator Implementations](tabularestimatortosupervisedadaptor/supervisedtabularestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SupervisedTabularEstimator](supervisedtabularestimator.md)

## See Also

- [struct TabularTransformerToEstimatorAdaptor](tabulartransformertoestimatoradaptor.md)
  A tabular estimator that always returns a predefined tabular transformer.
- [struct TabularTransformerToUpdatableEstimatorAdaptor](tabulartransformertoupdatableestimatoradaptor.md)
  An updatable tabular estimator that always returns a predefined transformer.
- [struct UpdatableTabularEstimatorToSupervisedAdaptor](updatabletabularestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable tabular estimator as an updatable supervised tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimatortosupervisedadaptor)*