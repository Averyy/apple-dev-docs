# join(with:on:type:)

**Framework**: Create ML  
**Kind**: method

Creates a new data table by merging two data tables by the given columns.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func join(with: MLDataTable, on columnsNamed: String..., type: MLDataTable.JoinType = .inner) -> MLDataTable
```

#### Return Value

A new data table.

## Parameters

- `with`: Another data table to merge with this data table.
- `columnsNamed`: If you do not provide any column names, the method uses all the columns present in both tables.
- `type`: The type of   operation, which are equivalent to SQL   types.

## See Also

- [MLDataTable.JoinType](mldatatable/jointype.md)
  Join types available for [`MLDataTable`](mldatatable.md) join operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/join(with:on:type:))*