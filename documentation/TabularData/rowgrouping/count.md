# count

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The number of groups in the row grouping.

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
var count: Int { get }
```

Available when `GroupingKey` conforms to `Hashable`.

## See Also

### Inspecting a row grouping
- [subscript(Int) -> (key: GroupingKey?, group: DataFrame.Slice)](./subscript%28_%29-5z2eg.md)
  Retrieves a group at an index.
- [subscript(Any?...) -> DataFrame.Slice?](./subscript%28_%29-2xxs8.md)
  Retrieves a group slice by key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/count)*