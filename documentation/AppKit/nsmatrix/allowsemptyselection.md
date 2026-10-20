# allowsEmptySelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a radio-mode matrix supports an empty selection.

**Availability**:
- macOS

## Declaration

```swift
var allowsEmptySelection: Bool { get set }
```

```objc
@property BOOL allowsEmptySelection;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the matrix allows one or zero cells to be selected. When the value of this property is [`true`](../../Swift/true.md), the matrix allows one and only one cell (not zero cells) to be selected. This setting has effect only in the `NSRadioModeMatrix` selection mode.

## See Also

### Configuring the Matrix Object
- [var mode: NSMatrix.Mode](./mode-swift.property.md)
  The selection mode of the receiver.
- [var isSelectionByRect: Bool](./isselectionbyrect.md)
  A Boolean that indicates whether the user can select a rectangle of cells in the receiver by dragging the cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/allowsemptyselection)*