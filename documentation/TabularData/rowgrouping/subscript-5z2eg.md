# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Retrieves a group at an index.

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
subscript(position: Int) -> (key: GroupingKey?, group: DataFrame.Slice) { get }
```

## Parameters

- `position`: A valid index to a group in the row grouping.

## See Also

- [var count: Int](rowgrouping/count.md)
  The number of groups in the row grouping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/subscript(_:)-5z2eg)*