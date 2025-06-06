# width(min:ideal:max:)

**Framework**: SwiftUI  
**Kind**: method

Creates a resizable table column with the provided constraints.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func width(min: CGFloat? = nil, ideal: CGFloat? = nil, max: CGFloat? = nil) -> TableColumn<RowValue, Sort, Content, Label>
```

#### Discussion

Always specify at least one width constraint when calling this method. Pass `nil` or leave out a constraint to indicate no change to the sizing of a column.

To create a fixed size column use [`width(_:)`](tablecolumn/width(_:).md) instead.

## Parameters

- `min`: The minimum width of a resizable column. If non- , the   value must be greater than or equal to  .
- `ideal`: The ideal width of the column, used to determine the initial   width of the table column. The column always starts at least as   large as the set ideal size, but may be larger if table was sized   larger than the ideal of all of its columns.
- `max`: The maximum width of a resizable column. If non- , the   value must be greater than  . Pass   doc://com.apple.documentation/documentation/CoreFoundation/CGFloat/1454161-infinity   to indicate unconstrained maximum width.

## See Also

- [func width(CGFloat?) -> TableColumn<RowValue, Sort, Content, Label>](tablecolumn/width(_:).md)
  Creates a fixed width table column that isn’t user resizable.
- [func width() -> TableColumn<RowValue, Sort, Content, Label>](tablecolumn/width.md)
  Sets the column’s width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/width(min:ideal:max:))*