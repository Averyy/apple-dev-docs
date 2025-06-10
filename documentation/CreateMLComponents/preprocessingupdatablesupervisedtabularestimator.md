# PreprocessingUpdatableSupervisedTabularEstimator

**Framework**: Create ML Components  
**Kind**: struct

An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator> where Preprocessor : TabularTransformer, Estimator : UpdatableSupervisedTabularEstimator
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingupdatablesupervisedtabularestimator/init(_:_:).md)
  Creates a composed supervised estimator from a preprocessing transformer and a supervised estimator.
### Getting the properties
- [var annotationColumnID: ColumnID<Estimator.Annotation>](preprocessingupdatablesupervisedtabularestimator/annotationcolumnid.md)
  The annotation column identifier.
- [var estimator: Estimator](preprocessingupdatablesupervisedtabularestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingupdatablesupervisedtabularestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encodeWithOptimizer(PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatablesupervisedtabularestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Preprocesing and fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingupdatablesupervisedtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame of examples.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new data frame of preprocessed features.
- [PreprocessingUpdatableSupervisedTabularEstimator.Annotation](preprocessingupdatablesupervisedtabularestimator/annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Input](preprocessingupdatablesupervisedtabularestimator/input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Intermediate](preprocessingupdatablesupervisedtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Output](preprocessingupdatablesupervisedtabularestimator/output.md)
  The output type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Transformer](preprocessingupdatablesupervisedtabularestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTabularEstimator Implementations](preprocessingupdatablesupervisedtabularestimator/supervisedtabularestimator-implementations.md)
- [UpdatableSupervisedTabularEstimator Implementations](preprocessingupdatablesupervisedtabularestimator/updatablesupervisedtabularestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedTabularEstimator](supervisedtabularestimator.md)
- [UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)

## See Also

- [protocol TabularTransformer](tabulartransformer.md)
  A tabular transformer that transforms a data frame.
- [protocol TabularEstimator](tabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [protocol SupervisedTabularEstimator](supervisedtabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [struct ColumnSelector](columnselector.md)
  An operation that applies an estimator to a selection of columns.
- [struct ColumnSelectorTransformer](columnselectortransformer.md)
  A transformer that applies a base transformer to specific columns in a data frame.
- [enum ColumnSelection](columnselection.md)
  A selection of columns from a data frame.
- [struct ColumnConcatenator](columnconcatenator.md)
  A transformer that concatenates every numerical column in a dataframe into to a shaped array for each row.
- [struct PreprocessingSupervisedTabularEstimator](preprocessingsupervisedtabularestimator.md)
  A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.
- [struct PreprocessingTabularEstimator](preprocessingtabularestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator)*