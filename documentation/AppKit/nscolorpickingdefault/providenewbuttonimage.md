# provideNewButtonImage()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Provides the image of the button used to select the receiver in the color panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func provideNewButtonImage() -> NSImage
```

#### Return Value

The image for the mode button the user uses to select this picker in the color panel; that is, the color picker’s representation in the  `NSMatrix` of the `NSColorPanel`.

#### Discussion

This image is the same one the color panel uses as an argument when sending the [`insertNewButtonImage(_:in:)`](nscolorpickingdefault/insertnewbuttonimage(_:in:).md) message.

## See Also

- [func setMode(NSColorPanel.Mode)](nscolorpickingdefault/setmode(_:).md)
  Specifies the receiver’s mode.
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](nscolorpickingdefault/insertnewbuttonimage(_:in:).md)
  Sets the image of a given button cell.
- [func minContentSize() -> NSSize](nscolorpickingdefault/mincontentsize.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](nscolorpickingdefault/buttontooltip.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/providenewbuttonimage())*