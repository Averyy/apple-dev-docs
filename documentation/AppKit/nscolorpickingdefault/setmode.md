# setMode(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Specifies the receiver’s mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setMode(_ mode: NSColorPanel.Mode)
```

#### Discussion

This method is invoked by the `NSColorPanel` method [`mode`](nscolorpanel/mode-swift.property.md) method to ensure the color picker reflects the current mode. For example, invoke this method during color picker initialization to ensure that all color pickers are restored to the mode the user left them in the last time an `NSColorPanel` was used.

Most color pickers have only one mode and thus don’t need to do any work in this method. An example of a color picker that uses this method is the slider picker, which can choose from one of several submodes depending on the value of `mode`.

## Parameters

- `mode`: The color picker mode. The available modes are described in  .

## See Also

- [func insertNewButtonImage(NSImage, in: NSButtonCell)](nscolorpickingdefault/insertnewbuttonimage(_:in:).md)
  Sets the image of a given button cell.
- [func provideNewButtonImage() -> NSImage](nscolorpickingdefault/providenewbuttonimage.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func minContentSize() -> NSSize](nscolorpickingdefault/mincontentsize.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](nscolorpickingdefault/buttontooltip.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/setmode(_:))*