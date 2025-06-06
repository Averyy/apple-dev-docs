# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Returns a column you select by its name.

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
subscript(columnName: String) -> AnyColumnSlice { get }
```

## Parameters

- `columnName`: The name of a column.

## See Also

- [subscript<T>(ColumnID<T>) -> DiscontiguousColumnSlice<T>](dataframe/slice/subscript(_:)-32h9z.md)
  Returns a column you select by its column identifier.
- [subscript<T>(column _: Int, T.Type) -> DiscontiguousColumnSlice<T>](dataframe/slice/subscript(column:_:).md)
  Returns a column you select by its index.
- [subscript<T>(String, T.Type) -> DiscontiguousColumnSlice<T>](dataframe/slice/subscript(_:_:).md)
  Returns a column you select by its name and type.
- [subscript(dynamicMember _: String) -> AnyColumnSlice](dataframe/slice/subscript(dynamicmember:).md)
  Returns a column you select by its name to support dynamic-member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/subscript(_:)-18kdy)*