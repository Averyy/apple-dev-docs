# insertNewButtonImage(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Sets the image of a given button cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertNewButtonImage(_ newButtonImage: NSImage, in buttonCell: NSButtonCell)
```

#### Discussion

This method should perform application-specific manipulation of the image before it’s inserted and displayed by the button cell.

## Parameters

- `newButtonImage`: The image to set for the button cell.
- `buttonCell`: The   object that lets the user choose the picker from the color panel—the color picker’s representation in the    of the  .

## See Also

- [func setMode(NSColorPanel.Mode)](nscolorpickingdefault/setmode(_:).md)
  Specifies the receiver’s mode.
- [func provideNewButtonImage() -> NSImage](nscolorpickingdefault/providenewbuttonimage.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func minContentSize() -> NSSize](nscolorpickingdefault/mincontentsize.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](nscolorpickingdefault/buttontooltip.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/insertnewbuttonimage(_:in:))*