# UpdatableTabularEstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An adaptor that exposes an updatable tabular estimator as an updatable supervised tabular estimator.

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
struct UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : UpdatableTabularEstimator, Annotation : Equatable
```

## Topics

### Creating an adaptor
- [init(Estimator, annotationColumnID: ColumnID<Annotation>)](./updatabletabularestimatortosupervisedadaptor/init%28_,annotationcolumnid%29.md)
  Creates an updatable tabular estimator supervised adaptor.
### Getting the properties
- [var annotationColumnID: ColumnID<Annotation>](./updatabletabularestimatortosupervisedadaptor/annotationcolumnid.md)
  The annotation column identifier.
- [let estimator: Estimator](./updatabletabularestimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](./updatabletabularestimatortosupervisedadaptor/encode%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./updatabletabularestimatortosupervisedadaptor/decode%28from%29.md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](./updatabletabularestimatortosupervisedadaptor/encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./updatabletabularestimatortosupervisedadaptor/decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer.
### Fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./updatabletabularestimatortosupervisedadaptor/fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a data frame.
- [func makeTransformer() -> Estimator.Transformer](./updatabletabularestimatortosupervisedadaptor/maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](./updatabletabularestimatortosupervisedadaptor/update%28_,with,eventhandler%29.md)
  Updates a transformer with a new data frame containing examples.
- [protocol Transformer](./transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SupervisedTabularEstimator](./supervisedtabularestimator.md)
- [UpdatableSupervisedTabularEstimator](./updatablesupervisedtabularestimator.md)

## See Also

### Tabular adaptors
- [struct TabularEstimatorToSupervisedAdaptor](./tabularestimatortosupervisedadaptor.md)
  An adaptor that exposes a tabular estimator as a tabular supervised estimator.
- [struct TabularTransformerToEstimatorAdaptor](./tabulartransformertoestimatoradaptor.md)
  A tabular estimator that always returns a predefined tabular transformer.
- [struct TabularTransformerToUpdatableEstimatorAdaptor](./tabulartransformertoupdatableestimatoradaptor.md)
  An updatable tabular estimator that always returns a predefined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor)*