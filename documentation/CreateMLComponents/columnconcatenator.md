# ColumnConcatenator

**Framework**: Create ML Components  
**Kind**: struct

A transformer that concatenates every numerical column in a dataframe into to a shaped array for each row.

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
struct ColumnConcatenator<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

#### Overview

The resulting concatenated column contains `MLShapedArray<Scalar>` elements. For example

```None
┏━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓
┃   ┃ label    ┃ price   ┃ rooms ┃ A     ┃ B     ┃ C     ┃
┃   ┃ <String> ┃ <Int>   ┃ <Int> ┃ <Int> ┃ <Int> ┃ <Int> ┃
┡━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━┩
│ 0 │ good     │ 850,000 │     4 │     1 │     0 │     0 │
│ 1 │ bad      │ 700,000 │     3 │     0 │     1 │     0 │
│ 2 │ bad      │ 650,000 │     3 │     0 │     0 │     1 │
│ 3 │ good     │ 600,000 │     2 │     0 │     1 │     0 │
└───┴──────────┴─────────┴───────┴───────┴───────┴───────┘
```

would be concatenated as:

```None
┏━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   ┃ label    ┃ features               ┃
┃   ┃ <String> ┃ <MLShapedArray<Float>> ┃
┡━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0 │ good     │ [850,000, 4, 1, 0, 0]  │
│ 1 │ bad      │ [700,000, 3, 0, 1, 0]  │
│ 2 │ bad      │ [650,000, 3, 0, 0, 1]  │
│ 3 │ good     │ [600,000, 2, 0, 1, 0]  │
└───┴──────────┴────────────────────────┘
```

Non-numerical columns are left in the data frame unchanged. Supported numeric types are `Int`, `UInt8`, `Float`, and `Double`. Arrays and shaped arrays of those types as supported, but every array in a given column must have the same shape and shaped arrays across columns must have the same shape except for the last dimension.

## Topics

### Creating the concatenator
- [init(columnSelection: ColumnSelection, concatenatedColumnName: String)](columnconcatenator/init(columnselection:concatenatedcolumnname:).md)
  Creates a concatenator that concatenates numeric columns into a new column of ML shaped array.
### Getting the properties
- [var columnSelection: ColumnSelection](columnconcatenator/columnselection.md)
  The selection of columns to concatenate.
- [var concatenatedColumnName: String](columnconcatenator/concatenatedcolumnname.md)
  The name of the concatenated column containing the shaped arrays.
### Applying
- [func applied(to: DataFrame, eventHandler: EventHandler?) throws -> DataFrame](columnconcatenator/applied(to:eventhandler:).md)
  Combines every numerical column in a data frame into to a shaped array for each row.
### Type Aliases
- [ColumnConcatenator.Input](columnconcatenator/input.md)
  The input type.
- [ColumnConcatenator.Output](columnconcatenator/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](columnconcatenator/customdebugstringconvertible-implementations.md)
- [TabularTransformer Implementations](columnconcatenator/tabulartransformer-implementations.md)
- [Transformer Implementations](columnconcatenator/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
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
- [struct ColumnSelectorTransformer](columnselectortransformer.md)
  A transformer that applies a base transformer to specific columns in a data frame.
- [enum ColumnSelection](columnselection.md)
  A selection of columns from a data frame.
- [struct PreprocessingSupervisedTabularEstimator](preprocessingsupervisedtabularestimator.md)
  A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.
- [struct PreprocessingTabularEstimator](preprocessingtabularestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnconcatenator)*