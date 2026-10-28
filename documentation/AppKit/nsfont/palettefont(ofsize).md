# paletteFont(ofSize:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the font used for palette window title bars, in the specified size.

**Availability**:
- macOS

## Declaration

```swift
class func paletteFont(ofSize fontSize: CGFloat) -> NSFont
```

```objc
+ (NSFont *) paletteFontOfSize:(CGFloat) fontSize;
```

## Return Value

A font object of the specified size.

## Discussion

If `fontSize` is 0 or negative, returns the palette title font at the default size.

## Parameters

- `fontSize`: The size in points to which the font is scaled.

## See Also

### Related Documentation
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates a font object for the specified font name and font size.
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
- [class func toolTipsFont(ofSize: CGFloat) -> NSFont](./tooltipsfont%28ofsize%29.md)
  Returns the font used for tool tips labels, in the specified size.
- [class var labelFontSize: CGFloat](./labelfontsize.md)
  Returns the size of the standard label font.
- [class func systemFontSize(for: NSControl.ControlSize) -> CGFloat](./systemfontsize%28for%29.md)
  Returns the font size used for the specified control size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/palettefont(ofsize:))*