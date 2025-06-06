# effectiveRowSizeStyle

**Framework**: AppKit  
**Kind**: property

The effective row size style for the table.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var effectiveRowSizeStyle: NSTableView.RowSizeStyle { get }
```

#### Discussion

If the value in the [`rowSizeStyle`](nstableview/rowsizestyle-swift.property.md) property is [`NSTableView.RowSizeStyle.default`](nstableview/rowsizestyle-swift.enum/default.md), then this property contains the default size for this  table. The default size is currently set in System Preferences by the user.

## See Also

- [var rowSizeStyle: NSTableView.RowSizeStyle](nstableview/rowsizestyle-swift.property.md)
  The row size style (small, medium, large, or custom) used by the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/effectiverowsizestyle)*