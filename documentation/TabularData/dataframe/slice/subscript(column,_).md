# subscript(column:_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

Returns a column you select by its index.

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
subscript<T>(column index: Int, type: T.Type) -> DiscontiguousColumnSlice<T> { get }
```

## Parameters

- `index`: The index of a column.

## See Also

### Creating a Slice by Selecting a Column
- [subscript<T>(ColumnID<T>) -> DiscontiguousColumnSlice<T>](./subscript%28_%29-32h9z.md)
  Returns a column you select by its column identifier.
- [subscript<T>(String, T.Type) -> DiscontiguousColumnSlice<T>](./subscript%28_,_%29.md)
  Returns a column you select by its name and type.
- [subscript(String) -> AnyColumnSlice](./subscript%28_%29-18kdy.md)
  Returns a column you select by its name.
- [subscript(dynamicMember _: String) -> AnyColumnSlice](./subscript%28dynamicmember%29.md)
  Returns a column you select by its name to support dynamic-member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/subscript(column:_:))*