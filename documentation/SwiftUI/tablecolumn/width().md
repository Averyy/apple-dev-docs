# width()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the column’s width.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

> **Deprecated**: Use [`width(_:)`](./width%28_%29.md) or [`width(min:ideal:max:)`](./width%28min,ideal,max%29.md) instead.

## Declaration

```swift
@export(implementation)
nonisolated func width() -> TableColumn<RowValue, Sort, Content, Label>
```

Available when `RowValue` conforms to `Identifiable`, `Sort` conforms to `SortComparator`, `Content` conforms to `View`, and `Label` conforms to `View`.

## See Also

### Setting the column width
- [func width(CGFloat?) -> TableColumn<RowValue, Sort, Content, Label>](./width%28_%29.md)
  Creates a fixed width table column that isn’t user resizable.
- [func width(min: CGFloat?, ideal: CGFloat?, max: CGFloat?) -> TableColumn<RowValue, Sort, Content, Label>](./width%28min,ideal,max%29.md)
  Creates a resizable table column with the provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/width())*