# effectiveRowSizeStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The effective row size style for the table.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var effectiveRowSizeStyle: NSTableView.RowSizeStyle { get }
```

```objc
@property (readonly) NSTableViewRowSizeStyle effectiveRowSizeStyle;
```

#### Discussion

If the value in the [`rowSizeStyle`](./rowsizestyle-swift.property.md) property is [`NSTableView.RowSizeStyle.default`](./rowsizestyle-swift.enum/default.md), then this property contains the default size for this  table. The default size is currently set in System Preferences by the user.

## See Also

### Getting and Setting Row Size Styles
- [var rowSizeStyle: NSTableView.RowSizeStyle](./rowsizestyle-swift.property.md)
  The row size style (small, medium, large, or custom) used by the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/effectiverowsizestyle)*