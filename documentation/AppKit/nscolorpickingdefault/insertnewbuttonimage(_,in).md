# insertNewButtonImage(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the image of a given button cell.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func insertNewButtonImage(_ newButtonImage: NSImage, in buttonCell: NSButtonCell)
```

```objc
- (void) insertNewButtonImage:(NSImage *) newButtonImage in:(NSButtonCell *) buttonCell;
```

#### Discussion

This method should perform application-specific manipulation of the image before it’s inserted and displayed by the button cell.

## Parameters

- `newButtonImage`: The image to set for the button cell.
- `buttonCell`: The `NSButtonCell` object that lets the user choose the picker from the color panel—the color picker’s representation in the  `NSMatrix` of the `NSColorPanel`.

## See Also

### Configuring Color Pickers
- [func setMode(NSColorPanel.Mode)](./setmode%28_%29.md)
  Specifies the receiver’s mode.
- [func provideNewButtonImage() -> NSImage](./providenewbuttonimage%28%29.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func minContentSize() -> NSSize](./mincontentsize%28%29.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](./buttontooltip%28%29.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/insertnewbuttonimage(_:in:))*