# isSelectionByRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user can select a rectangle of cells in the receiver by dragging the cursor.

**Availability**:
- macOS

## Declaration

```swift
var isSelectionByRect: Bool { get set }
```

```objc
@property (getter=isSelectionByRect) BOOL selectionByRect;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the matrix allows the user to select a rectangle of cells by dragging. When the value of this property is [`false`](../../Swift/false.md), selection in the matrix is on a row-by-row basis. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](./setselectionfrom%28_,to,anchor,highlight%29.md)
  Programmatically selects a range of cells.
### Configuring the Matrix Object
- [var mode: NSMatrix.Mode](./mode-swift.property.md)
  The selection mode of the receiver.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/isselectionbyrect)*