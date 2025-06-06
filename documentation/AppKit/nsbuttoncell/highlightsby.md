# highlightsBy

**Framework**: AppKit  
**Kind**: property

A set of flags that indicate how the button highlights when it receives a mouse-down event (that is, when the button is pressed).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var highlightsBy: NSCell.StyleMask { get set }
```

#### Discussion

The value of this property is the logical OR of one or more of flags described in the “Constants” section of [`NSCell`](nscell.md).

If both `NSChangeGrayCellMask` and `NSChangeBackgroundCellMask` are specified, both are recorded, but the resulting behavior depends on the button cell’s image. If the button has no image, or if the image has no alpha (transparency) data, `NSChangeGrayCellMask` is used; if the image has alpha data, `NSChangeBackgroundCellMask` is used. This arrangement allows the color swap of the background to show through the image’s transparent pixels.

## See Also

- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var showsStateBy: NSCell.StyleMask](nsbuttoncell/showsstateby.md)
  The flags that indicate how the button cell shows its alternate state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/highlightsby)*