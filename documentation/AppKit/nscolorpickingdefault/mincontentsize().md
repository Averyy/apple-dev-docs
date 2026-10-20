# minContentSize()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates the receiver’s minimum content size.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func minContentSize() -> NSSize
```

```objc
- (NSSize) minContentSize;
```

#### Discussion

The receiver does not allow a size smaller than `minContentSize`.

## See Also

### Configuring Color Pickers
- [func setMode(NSColorPanel.Mode)](./setmode%28_%29.md)
  Specifies the receiver’s mode.
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./insertnewbuttonimage%28_,in%29.md)
  Sets the image of a given button cell.
- [func provideNewButtonImage() -> NSImage](./providenewbuttonimage%28%29.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func buttonToolTip() -> String](./buttontooltip%28%29.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/mincontentsize())*