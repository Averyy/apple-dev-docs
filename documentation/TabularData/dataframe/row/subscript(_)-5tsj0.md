# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a value at a column index.

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
subscript(position: Int) -> Any? { get set }
```

## Parameters

- `position`: A valid index to a column in the row.

## See Also

### Accessing elements
- [subscript(String) -> Any?](./subscript%28_%29-2v7qz.md)
  Accesses a value in the row you select by a column name.
- [subscript<T>(String, T.Type) -> T?](./subscript%28_,_%29-7gpc3.md)
  Accesses a value in the row you select by a column name and type.
- [subscript<T>(ColumnID<T>) -> T?](./subscript%28_%29-9o424.md)
  Accesses a value in the row you select by a column identifier.
- [subscript<T>(Int, T.Type) -> T?](./subscript%28_,_%29-1o38p.md)
  Accesses a value in the row you select by a column index and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/row/subscript(_:)-5tsj0)*