# PreprocessingTabularEstimator

**Framework**: Create ML Components  
**Kind**: struct

An estimator that composes a preprocessing transformer and an estimator.

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
struct PreprocessingTabularEstimator<Preprocessor, Estimator> where Preprocessor : TabularTransformer, Estimator : TabularEstimator
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingtabularestimator/init(_:_:).md)
  Creates a composed estimator from a preprocessing transformer and an estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingtabularestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingtabularestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encode(PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.
### Preprocesing and fitting
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed features.
- [PreprocessingTabularEstimator.Input](preprocessingtabularestimator/input.md)
  The input type.
- [PreprocessingTabularEstimator.Intermediate](preprocessingtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTabularEstimator.Output](preprocessingtabularestimator/output.md)
  The output type.
- [PreprocessingTabularEstimator.Transformer](preprocessingtabularestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [TabularEstimator Implementations](preprocessingtabularestimator/tabularestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabularEstimator](tabularestimator.md)

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
- [struct PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator)*