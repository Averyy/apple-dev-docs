# startIndex

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The index of the initial group in the row grouping.

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
var startIndex: Int { get }
```

Available when `GroupingKey` conforms to `Hashable`.

## See Also

### Retrieving an Index
- [var endIndex: Int](./endindex.md)
  The index of the final group in the row grouping.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the index immediately after an element index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/startindex)*