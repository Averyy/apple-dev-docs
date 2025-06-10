# ColumnSelector

**Framework**: Create ML Components  
**Kind**: struct

An operation that applies an estimator to a selection of columns.

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
struct ColumnSelector<Estimator, UnwrappedInput> where Estimator : Estimator, Estimator.Transformer.Input == UnwrappedInput?
```

#### Overview

This estimator applies a non-tabular estimator to a selection of columns. Here’s an example of normalizing numeric values within each column using a [`StandardScaler`](standardscaler.md):

```None
let numericalScaling = ColumnSelector(
    columns: ["volume", "price"],
    estimator: NumericImputer<Float>(.mean)
        .appending(StandardScaler<Float>())
)
```

In most cases, an inputer must handle missing values.

## Topics

### Creating the selection
- [init(columns: [String], estimator: Estimator)](columnselector/init(columns:estimator:).md)
  Creates a select operation with an estimator.
- [init(ColumnSelection, estimator: Estimator)](columnselector/init(_:estimator:).md)
  Creates a select operation with an estimator.
- [init<T>(ColumnSelection, transformer: T)](columnselector/init(_:transformer:).md)
  Creates a select operation with a transformer.
### Getting the properties
- [var columnSelection: ColumnSelection](columnselector/columnselection.md)
  The column selection strategy.
- [var estimator: Estimator](columnselector/estimator.md)
  The estimator to use on each column.
### Encoding and decoding
- [func encode(ColumnSelector<Estimator, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](columnselector/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> ColumnSelector<Estimator, UnwrappedInput>.Transformer](columnselector/decode(from:).md)
  Decodes a previously fitted transformer.
### Fitting a transformer
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> ColumnSelector<Estimator, UnwrappedInput>.Transformer](columnselector/fitted(to:eventhandler:).md)
  Fits a transformer to a data frame
- [ColumnSelector.Input](columnselector/input.md)
- [ColumnSelector.Output](columnselector/output.md)
- [ColumnSelector.Transformer](columnselector/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [TabularEstimator Implementations](columnselector/tabularestimator-implementations.md)
- [UpdatableTabularEstimator Implementations](columnselector/updatabletabularestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselector)*