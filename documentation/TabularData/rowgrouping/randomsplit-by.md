# randomSplit(by:)

**Framework**: TabularData  
**Kind**: method

Generates two row groupings by randomly splitting the original with a proportion.

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
func randomSplit(by proportion: Double) -> (Self, Self)
```

#### Return Value

A tuple of two row groupings.

## See Also

- [func randomSplit(by: Double, seed: Int?) -> (RowGrouping<GroupingKey>, RowGrouping<GroupingKey>)](rowgrouping/randomsplit(by:seed:).md)
  Generates two row groupings by randomly splitting the original with a proportion and a seed number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/randomsplit(by:))*