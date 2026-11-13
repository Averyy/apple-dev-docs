# removeColumn(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Removes a column you select by its column identifier from the data frame.

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
@discardableResult
mutating func removeColumn<T>(_ id: ColumnID<T>) -> Column<T>
```

## Return Value

The column the method removes from the data frame.

## Parameters

- `id`: The identifier of a column in the data frame.

## See Also

### Removing a column
- [func removeColumn(String) -> AnyColumn](./removecolumn%28_%29-5zu7l.md)
  Removes a column you select by its name from the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/removecolumn(_:)-qtea)*