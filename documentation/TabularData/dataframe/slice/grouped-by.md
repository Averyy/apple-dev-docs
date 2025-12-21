# grouped(by:)

**Framework**: TabularData  
**Kind**: method

Creates a grouping of rows that the method selects by choosing unique values in a column.

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
func grouped(by columnName: String) -> any RowGroupingProtocol
```

## Parameters

- `columnName`: The name of a column.

## See Also

- [struct RowGrouping](rowgrouping.md)
  A collection of row selections that have the same value in a column.
- [protocol RowGroupingProtocol](rowgroupingprotocol.md)
  A type that represents a collection of row selections that have the same value in a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/grouped(by:))*