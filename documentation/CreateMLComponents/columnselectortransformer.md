# ColumnSelectorTransformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that applies a base transformer to specific columns in a data frame.

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
struct ColumnSelectorTransformer<Base, UnwrappedInput> where Base : Transformer, Base.Input == UnwrappedInput?
```

## Topics

### Creating the transformer
- [init(transformers: [String : Base], columnMapping: [String : String])](columnselectortransformer/init(transformers:columnmapping:).md)
  Creates a select transformer.
### Getting the properties
- [var columnMapping: [String : String]](columnselectortransformer/columnmapping.md)
  A mapping of input column names to output column names.
- [var transformers: [String : Base]](columnselectortransformer/transformers.md)
  A dictionary of column names to transformers.
### Applying a transformation
- [func applied(to: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](columnselectortransformer/applied(to:eventhandler:).md)
  Performs the transformation on selected columns of the data frame.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabularTransformer](tabulartransformer.md)
- [Transformer](transformer.md)

## See Also

- [protocol TabularTransformer](tabulartransformer.md)
  A tabular transformer that transforms a data frame.
- [protocol TabularEstimator](tabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [protocol SupervisedTabularEstimator](supervisedtabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [struct ColumnSelector](columnselector.md)
  An operation that applies an estimator to a selection of columns.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselectortransformer)*