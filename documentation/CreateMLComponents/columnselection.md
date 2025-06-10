# ColumnSelection

**Framework**: Create ML Components  
**Kind**: enum

A selection of columns from a data frame.

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
enum ColumnSelection
```

## Topics

### Column selection types
- [ColumnSelection.all](columnselection/all.md)
  Select all columns in the data frame.
- [ColumnSelection.exclude(columnNames:)](columnselection/exclude(columnnames:).md)
  Selects all columns except the specified columns.
- [ColumnSelection.include(columnNames:)](columnselection/include(columnnames:).md)
  Selects only the specified columns.
- [ColumnSelection.numeric](columnselection/numeric.md)
  Select all numeric columns in the data frame.
### Creating a column selection
- [init(from: any Decoder) throws](columnselection/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](columnselection/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselection)*