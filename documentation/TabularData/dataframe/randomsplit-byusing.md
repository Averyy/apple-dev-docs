# randomSplit(by:using:)

**Framework**: TabularData  
**Kind**: method

Generates two data frame slices by randomly splitting the rows of the data table type with a random-number generator.

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
func randomSplit<G>(by proportion: Double, using generator: inout G) -> (DataFrame.Slice, DataFrame.Slice) where G : RandomNumberGenerator
```

#### Return Value

A tuple of two data frame slices.

## Parameters

- `proportion`: A proportion in the range  .
- `generator`: A random-number generator.

## See Also

- [func randomSplit(by: Double, seed: Int?) -> (DataFrame.Slice, DataFrame.Slice)](dataframe/randomsplit(by:seed:).md)
  Generates two data frame slices by randomly splitting the rows of the data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/randomsplit(by:using:))*