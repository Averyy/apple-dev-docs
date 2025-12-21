# isSelectionByRect

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the user can select a rectangle of cells in the receiver by dragging the cursor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isSelectionByRect: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the matrix allows the user to select a rectangle of cells by dragging. When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), selection in the matrix is on a row-by-row basis. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](nsmatrix/setselectionfrom(_:to:anchor:highlight:).md)
  Programmatically selects a range of cells.
- [var mode: NSMatrix.Mode](nsmatrix/mode-swift.property.md)
  The selection mode of the receiver.
- [var allowsEmptySelection: Bool](nsmatrix/allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/isselectionbyrect)*