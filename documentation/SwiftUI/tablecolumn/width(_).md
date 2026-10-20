# width(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Creates a fixed width table column that isn’t user resizable.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func width(_ width: CGFloat? = nil) -> TableColumn<RowValue, Sort, Content, Label>
```

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to `SortComparator`, `Content` conforms to `View`, and `Label` conforms to `View`.

## Parameters

- `width`: A fixed width for the resulting column. If `width` is `nil`, the resulting column has no change in sizing.

## See Also

### Setting the column width
- [func width(min: CGFloat?, ideal: CGFloat?, max: CGFloat?) -> TableColumn<RowValue, Sort, Content, Label>](./width%28min,ideal,max%29.md)
  Creates a resizable table column with the provided constraints.
- [func width() -> TableColumn<RowValue, Sort, Content, Label>](./width%28%29.md)
  Sets the column’s width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/width(_:))*