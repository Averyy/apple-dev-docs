# index(before:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns the index immediately before an element index.

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
func index(before i: Int) -> Int
```

Available when `GroupingKey` conforms to `Hashable`.

## Parameters

- `i`: A valid index to an element in the column.

## See Also

### Retrieving an Index
- [var startIndex: Int](./startindex.md)
  The index of the initial group in the row grouping.
- [var endIndex: Int](./endindex.md)
  The index of the final group in the row grouping.
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the index immediately after an element index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/index(before:))*