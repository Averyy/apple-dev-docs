# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a column by its column identifier.

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
subscript<T>(id: ColumnID<T>) -> Column<T> { get set }
```

## Parameters

- `id`: The identifier of a column.

## See Also

### Accessing a column
- [subscript(String) -> AnyColumn](./subscript%28_%29-738lb.md)
  Accesses a column by its name.
- [subscript<T>(String, T.Type) -> Column<T>](./subscript%28_,_%29-5walz.md)
  Accesses a column by its name and type.
- [subscript(column _: Int) -> AnyColumn](./subscript%28column%29.md)
  Accesses a column by its index.
- [subscript<T>(column _: Int, T.Type) -> Column<T>](./subscript%28column,_%29.md)
  Accesses a column by its index and type.
- [subscript(dynamicMember _: String) -> AnyColumn](./subscript%28dynamicmember%29.md)
  Accesses a column by its name to support dynamic-member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/subscript(_:)-6mv5i)*