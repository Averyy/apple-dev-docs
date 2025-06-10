# PreprocessingSupervisedTabularEstimator

**Framework**: Create ML Components  
**Kind**: struct

A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.

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
struct PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator> where Preprocessor : TabularTransformer, Estimator : SupervisedTabularEstimator
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingsupervisedtabularestimator/init(_:_:).md)
  Creates a composed supervised tabular estimator from a preprocessing transformer and a supervised tabular estimator.
### Getting the properties
- [var annotationColumnID: ColumnID<Estimator.Annotation>](preprocessingsupervisedtabularestimator/annotationcolumnid.md)
  The annotation column identifier.
- [var estimator: Estimator](preprocessingsupervisedtabularestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingsupervisedtabularestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/decode(from:).md)
  Decodes a previously fitted transformer.
- [func encode(PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingsupervisedtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.
### Preprocesing and fitting
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingsupervisedtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed examples while validating.
- [PreprocessingSupervisedTabularEstimator.Annotation](preprocessingsupervisedtabularestimator/annotation.md)
  The annotation type.
- [PreprocessingSupervisedTabularEstimator.Input](preprocessingsupervisedtabularestimator/input.md)
  The input type.
- [PreprocessingSupervisedTabularEstimator.Intermediate](preprocessingsupervisedtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedTabularEstimator.Output](preprocessingsupervisedtabularestimator/output.md)
  The output type.
- [PreprocessingSupervisedTabularEstimator.Transformer](preprocessingsupervisedtabularestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTabularEstimator Implementations](preprocessingsupervisedtabularestimator/supervisedtabularestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedTabularEstimator](supervisedtabularestimator.md)

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
- [struct PreprocessingTabularEstimator](preprocessingtabularestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator)*