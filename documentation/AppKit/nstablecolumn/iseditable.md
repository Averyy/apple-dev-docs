# isEditable

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether a cell-based table’s column cells are user editable.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isEditable: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the user can edit cells in the cell-based table’s column. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

To initiate editing programmatically regardless of the value of this property, use the `NSTableView` [`editColumn(_:row:with:select:)`](nstableview/editcolumn(_:row:with:select:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/iseditable)*