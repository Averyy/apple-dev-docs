# isEditable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a cell-based table’s column cells are user editable.

**Availability**:
- macOS

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (getter=isEditable) BOOL editable;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the user can edit cells in the cell-based table’s column. The default value of this property is [`true`](../../Swift/true.md).

To initiate editing programmatically regardless of the value of this property, use the `NSTableView` [`editColumn(_:row:with:select:)`](../nstableview/editcolumn%28_,row,with,select%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/iseditable)*