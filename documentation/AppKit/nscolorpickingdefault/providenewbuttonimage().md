# provideNewButtonImage()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the image of the button used to select the receiver in the color panel.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func provideNewButtonImage() -> NSImage
```

```objc
- (NSImage *) provideNewButtonImage;
```

## Return Value

The image for the mode button the user uses to select this picker in the color panel; that is, the color picker’s representation in the  `NSMatrix` of the `NSColorPanel`.

## Discussion

This image is the same one the color panel uses as an argument when sending the [`insertNewButtonImage(_:in:)`](./insertnewbuttonimage%28_,in%29.md) message.

## See Also

### Configuring Color Pickers
- [func setMode(NSColorPanel.Mode)](./setmode%28_%29.md)
  Specifies the receiver’s mode.
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./insertnewbuttonimage%28_,in%29.md)
  Sets the image of a given button cell.
- [func minContentSize() -> NSSize](./mincontentsize%28%29.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](./buttontooltip%28%29.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/providenewbuttonimage())*