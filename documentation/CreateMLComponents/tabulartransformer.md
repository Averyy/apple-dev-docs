# TabularTransformer

**Framework**: Create ML Components  
**Kind**: protocol

A tabular transformer that transforms a data frame.

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
protocol TabularTransformer : Transformer where Self.Input == DataFrame, Self.Output == DataFrame
```

#### Overview

Tabular transformers represent operations on data frames. They modify and operate on values on one or more columns.

## Topics

### Appending
- [func appending(_:)](tabulartransformer/appending(_:).md)
  Composes this tabular transformer with another tabular transformer.
### Adapting
- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](tabulartransformer/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](tabulartransformer/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.
### Transforming
- [func callAsFunction(DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](tabulartransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
### Exporting
- [func export(to: URL) throws](tabulartransformer/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](tabulartransformer/export(to:metadata:).md)
  Exports this tabular transformer as a CoreML model with userInfo.

## Relationships

### Inherits From
- [Transformer](transformer.md)
### Conforming Types
- [ColumnConcatenator](columnconcatenator.md)
- [ColumnSelectorTransformer](columnselectortransformer.md)
- [ComposedTabularTransformer](composedtabulartransformer.md)
- [TreeClassifierModel](treeclassifiermodel.md)
- [TreeRegressorModel](treeregressormodel.md)

## See Also

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
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformer)*