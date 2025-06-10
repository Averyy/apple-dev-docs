# PreprocessingUpdatableTabularEstimator

**Framework**: Create ML Components  
**Kind**: struct

An updatable estimator that composes a preprocessing transformer and an updatable estimator.

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
struct PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator> where Preprocessor : TabularTransformer, Estimator : UpdatableTabularEstimator
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingupdatabletabularestimator/init(_:_:).md)
  Creates a composed updatable estimator from a preprocessing transformer and an estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingupdatabletabularestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingupdatabletabularestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatabletabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encodeWithOptimizer(PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingupdatabletabularestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer.
### Preprocesing and fitting
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingupdatabletabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed features.
- [func update(inout PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatabletabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame of examples.
- [func update(inout PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatabletabularestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new data frame of preprocessed features.
- [func makeTransformer() -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [PreprocessingUpdatableTabularEstimator.Input](preprocessingupdatabletabularestimator/input.md)
  The input type.
- [PreprocessingUpdatableTabularEstimator.Intermediate](preprocessingupdatabletabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableTabularEstimator.Output](preprocessingupdatabletabularestimator/output.md)
  The output type.
- [PreprocessingUpdatableTabularEstimator.Transformer](preprocessingupdatabletabularestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [TabularEstimator Implementations](preprocessingupdatabletabularestimator/tabularestimator-implementations.md)
- [UpdatableTabularEstimator Implementations](preprocessingupdatabletabularestimator/updatabletabularestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabularEstimator](tabularestimator.md)
- [UpdatableTabularEstimator](updatabletabularestimator.md)

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
- [struct PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator)*