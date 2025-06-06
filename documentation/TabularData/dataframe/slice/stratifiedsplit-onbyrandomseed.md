# stratifiedSplit(on:by:randomSeed:)

**Framework**: TabularData  
**Kind**: method

Generates two data frames by randomly splitting the rows of a column, which you select by its name, into strata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func stratifiedSplit(on columnName: String, by proportion: Double, randomSeed: Int? = nil) -> (DataFrame, DataFrame)
```

#### Return Value

A tuple of two data frames.

## Parameters

- `columnName`: The name of a column in the data frame type.
- `proportion`: A proportion in the range  .
- `randomSeed`: A seed number for a random-number generator.

## See Also

- [func stratifiedSplit<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of two columns, which you select by column identifiers, into strata.
- [func stratifiedSplit<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframe/slice/stratifiedsplit(on:_:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of three columns, which you select by column identifiers, into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/stratifiedsplit(on:by:randomseed:))*