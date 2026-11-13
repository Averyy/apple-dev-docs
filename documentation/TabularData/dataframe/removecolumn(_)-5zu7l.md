# removeColumn(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Removes a column you select by its name from the data frame.

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
mutating func removeColumn(_ name: String) -> AnyColumn
```

## Return Value

The column the method removes from the data frame.

## Parameters

- `name`: The name of a column in the data frame.

## See Also

### Removing a column
- [func removeColumn<T>(ColumnID<T>) -> Column<T>](./removecolumn%28_%29-qtea.md)
  Removes a column you select by its column identifier from the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/removecolumn(_:)-5zu7l)*