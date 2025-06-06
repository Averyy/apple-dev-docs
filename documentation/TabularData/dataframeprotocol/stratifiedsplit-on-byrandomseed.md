# stratifiedSplit(on:_:_:by:randomSeed:)

**Framework**: TabularData  
**Kind**: method

Generates two data frames by randomly splitting the rows of three columns, which you select by column identifiers, into strata.

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
func stratifiedSplit<T0, T1, T2>(on columnID0: ColumnID<T0>, _ columnID1: ColumnID<T1>, _ columnID2: ColumnID<T2>, by proportion: Double, randomSeed: Int? = nil) -> (DataFrame, DataFrame) where T0 : Hashable, T1 : Hashable, T2 : Hashable
```

#### Return Value

A tuple of two data frames.

## Parameters

- `columnID0`: A column identifier.
- `columnID1`: A second column identifier.
- `columnID2`: A third column identifier.
- `proportion`: A proportion in the range  .
- `randomSeed`: A seed number for a random-number generator.

## See Also

- [func stratifiedSplit(on: String, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:by:randomseed:)-9iauf.md)
  Generates two data frames by randomly splitting the rows of a column, which you select by its name, into strata.
- [func stratifiedSplit(on: String..., by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:by:randomseed:)-8szu1.md)
  Generates two data frames by randomly splitting the rows of multiple columns, which you select by their names, into strata.
- [func stratifiedSplit<T>(on: ColumnID<T>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:by:randomseed:)-714jk.md)
  Generates two data frames by randomly splitting the rows of a column, which you select by column identifier, into strata.
- [func stratifiedSplit<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, by: Double, randomSeed: Int?) -> (DataFrame, DataFrame)](dataframeprotocol/stratifiedsplit(on:_:by:randomseed:).md)
  Generates two data frames by randomly splitting the rows of two columns, which you select by column identifiers, into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframeprotocol/stratifiedsplit(on:_:_:by:randomseed:))*