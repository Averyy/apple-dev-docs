# minContentSize()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Indicates the receiver’s minimum content size.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func minContentSize() -> NSSize
```

#### Discussion

The receiver does not allow a size smaller than `minContentSize`.

## See Also

- [func setMode(NSColorPanel.Mode)](nscolorpickingdefault/setmode(_:).md)
  Specifies the receiver’s mode.
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](nscolorpickingdefault/insertnewbuttonimage(_:in:).md)
  Sets the image of a given button cell.
- [func provideNewButtonImage() -> NSImage](nscolorpickingdefault/providenewbuttonimage.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func buttonToolTip() -> String](nscolorpickingdefault/buttontooltip.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/mincontentsize())*