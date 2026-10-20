# buttonToolTip()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the toolbar button help tag.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func buttonToolTip() -> String
```

```objc
- (NSString *) buttonToolTip;
```

#### Return Value

Help tag text.

## See Also

### Configuring Color Pickers
- [func setMode(NSColorPanel.Mode)](./setmode%28_%29.md)
  Specifies the receiver’s mode.
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./insertnewbuttonimage%28_,in%29.md)
  Sets the image of a given button cell.
- [func provideNewButtonImage() -> NSImage](./providenewbuttonimage%28%29.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func minContentSize() -> NSSize](./mincontentsize%28%29.md)
  Indicates the receiver’s minimum content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/buttontooltip())*