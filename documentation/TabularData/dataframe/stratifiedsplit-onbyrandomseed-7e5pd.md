# stratifiedSplit(on:by:randomSeed:)

**Framework**: TabularData  
**Kind**: method

Generates two data frames by randomly splitting the rows of a column, which you select by column identifier, into strata.

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
func stratifiedSplit<T>(on columnID: ColumnID<T>, by proportion: Double, randomSeed: Int? = nil) -> (DataFrame, DataFrame) where T : Hashable
```

#### Return Value

A tuple of two data frames.

## Parameters

- `columnID`: A column identifier.
- `proportion`: A proportion in the range  .
- `randomSeed`: A seed number for a random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/stratifiedsplit(on:by:randomseed:)-7e5pd)*