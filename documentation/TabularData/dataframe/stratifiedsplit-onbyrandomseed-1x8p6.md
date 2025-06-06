# stratifiedSplit(on:by:randomSeed:)

**Framework**: TabularData  
**Kind**: method

Generates two data frames by randomly splitting the rows of multiple columns, which you select by their names, into strata.

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
func stratifiedSplit(on columnNames: String..., by proportion: Double, randomSeed: Int? = nil) -> (DataFrame, DataFrame)
```

#### Return Value

A tuple of two data frames.

## Parameters

- `columnNames`: A comma-separated, or variadic, list of column names.
- `proportion`: A proportion in the range  .
- `randomSeed`: A seed number for a random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/stratifiedsplit(on:by:randomseed:)-1x8p6)*