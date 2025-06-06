# randomSplit(by:seed:)

**Framework**: TabularData  
**Kind**: method

Generates two row groupings by randomly splitting the original with a proportion and a seed number.

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
func randomSplit(by proportion: Double, seed: Int? = nil) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)
```

#### Return Value

A tuple of two row groupings.

## Parameters

- `proportion`: A proportion in the range  .
- `seed`: A seed number for a random-number generator.

## See Also

- [func randomSplit(by: Double) -> (Self, Self)](rowgrouping/randomsplit(by:).md)
  Generates two row groupings by randomly splitting the original with a proportion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/randomsplit(by:seed:))*