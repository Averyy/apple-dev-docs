# rowSizeStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the row size style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var rowSizeStyle: NSTableView.RowSizeStyle { get set }
```

```objc
@property NSTableViewRowSizeStyle rowSizeStyle;
```

## Discussion

The `rowSizeStyle` property is set by the `NSTableView` to its [`effectiveRowSizeStyle`](../nstableview/effectiverowsizestyle.md). The cell view will layout the [`textField`](./textfield.md) and [`imageView`](./imageview.md) based on the `rowSizeStyle`.

A value of [`NSTableView.RowSizeStyle.default`](../nstableview/rowsizestyle-swift.enum/default.md) should never be set on the cell view, as it is an appropriate value only for the table as it returns the effective row size style for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/rowsizestyle)*