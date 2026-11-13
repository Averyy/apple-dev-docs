# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Retrieves a group slice by key.

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
subscript(keys: Any?...) -> DataFrame.Slice? { get }
```

## Parameters

- `keys`: A comma-separated, or variadic, list of key optionals.

## See Also

### Inspecting a row grouping
- [var count: Int](./count.md)
  The number of groups in the row grouping.
- [subscript(Int) -> (key: GroupingKey?, group: DataFrame.Slice)](./subscript%28_%29-5z2eg.md)
  Retrieves a group at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/subscript(_:)-2xxs8)*