# showsStateBy

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The flags that indicate how the button cell shows its alternate state.

**Availability**:
- macOS

## Declaration

```swift
var showsStateBy: NSCell.StyleMask { get set }
```

```objc
@property NSCellStyleMask showsStateBy;
```

## Discussion

The value of this property is the logical `OR` of one or more of the cell masks described in the “Constants” section of [`NSCell`](../nscell.md).

If both `NSChangeGrayCellMask` and `NSChangeBackgroundCellMask` are specified, both are recorded, but the actual behavior depends on the button cell’s image. If the button has no image, or if the image has no alpha (transparency) data, `NSChangeGrayCellMask` is used. If the image exists and has alpha data, `NSChangeBackgroundCellMask` is used; this arrangement allows the color swap of the background to show through the image’s transparent pixels.

## See Also

### Displaying the Cell
- [var highlightsBy: NSCell.StyleMask](./highlightsby.md)
  A set of flags that indicate how the button highlights when it receives a mouse-down event (that is, when the button is pressed).
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/showsstateby)*