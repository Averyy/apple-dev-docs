# systemFontSize(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the font size used for the specified control size.

**Availability**:
- macOS

## Declaration

```swift
class func systemFontSize(for controlSize: NSControl.ControlSize) -> CGFloat
```

```objc
+ (CGFloat) systemFontSizeForControlSize:(NSControlSize) controlSize;
```

#### Return Value

The font size in points for the specified control size.

#### Discussion

If `controlSize` does not correspond to a valid `NSControlSize`, returns the size of the standard system font.

## Parameters

- `controlSize`: The control size constant.

## See Also

### Creating UI Element Fonts
- [class func labelFont(ofSize: CGFloat) -> NSFont](./labelfont%28ofsize%29.md)
  Returns the font used for standard interface labels in the specified size.
- [class func messageFont(ofSize: CGFloat) -> NSFont](./messagefont%28ofsize%29.md)
  Returns the font used for standard interface items, such as button labels, menu items, and so on, in the specified size.
- [class func menuBarFont(ofSize: CGFloat) -> NSFont](./menubarfont%28ofsize%29.md)
  Returns the font used for menu bar items, in the specified size.
- [class func menuFont(ofSize: CGFloat) -> NSFont](./menufont%28ofsize%29.md)
  Returns the font used for menu items, in the specified size.
- [class func controlContentFont(ofSize: CGFloat) -> NSFont](./controlcontentfont%28ofsize%29.md)
  Returns the font used for the content of controls in the specified size.
- [class func titleBarFont(ofSize: CGFloat) -> NSFont](./titlebarfont%28ofsize%29.md)
  Returns the font used for window title bars, in the specified size.
- [class func paletteFont(ofSize: CGFloat) -> NSFont](./palettefont%28ofsize%29.md)
  Returns the font used for palette window title bars, in the specified size.
- [class func toolTipsFont(ofSize: CGFloat) -> NSFont](./tooltipsfont%28ofsize%29.md)
  Returns the font used for tool tips labels, in the specified size.
- [class var labelFontSize: CGFloat](./labelfontsize.md)
  Returns the size of the standard label font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/systemfontsize(for:))*