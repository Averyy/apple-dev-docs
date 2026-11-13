# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a value in the row you select by a column name.

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
subscript(columnName: String) -> Any? { get set }
```

## Parameters

- `columnName`: The name of a column.

## See Also

### Accessing elements
- [subscript(Int) -> Any?](./subscript%28_%29-5tsj0.md)
  Accesses a value at a column index.
- [subscript<T>(String, T.Type) -> T?](./subscript%28_,_%29-7gpc3.md)
  Accesses a value in the row you select by a column name and type.
- [subscript<T>(ColumnID<T>) -> T?](./subscript%28_%29-9o424.md)
  Accesses a value in the row you select by a column identifier.
- [subscript<T>(Int, T.Type) -> T?](./subscript%28_,_%29-1o38p.md)
  Accesses a value in the row you select by a column index and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/row/subscript(_:)-2v7qz)*