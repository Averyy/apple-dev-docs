# labelFont(ofSize:)

**Framework**: AppKit  
**Kind**: method

Returns the font used for standard interface labels in the specified size.

**Availability**:
- macOS ?+

## Declaration

```swift
class func labelFont(ofSize fontSize: CGFloat) -> NSFont
```

#### Return Value

A font object of the specified size. If `fontSize` is 0 or negative, returns the label font with the default size.

#### Discussion

The label font (Lucida Grande Regular 10 point) is used for the labels on toolbar buttons and to label tick marks on full-size sliders. For more information on system fonts, see Human Interface Guidelines > [`Typography`](https://developer.apple.com/design/human-interface-guidelines/typography).

## Parameters

- `fontSize`: The size in points to which the font is scaled.

## See Also

- [class func messageFont(ofSize: CGFloat) -> NSFont](nsfont/messagefont(ofsize:).md)
  Returns the font used for standard interface items, such as button labels, menu items, and so on, in the specified size.
- [class func menuBarFont(ofSize: CGFloat) -> NSFont](nsfont/menubarfont(ofsize:).md)
  Returns the font used for menu bar items, in the specified size.
- [class func menuFont(ofSize: CGFloat) -> NSFont](nsfont/menufont(ofsize:).md)
  Returns the font used for menu items, in the specified size.
- [class func controlContentFont(ofSize: CGFloat) -> NSFont](nsfont/controlcontentfont(ofsize:).md)
  Returns the font used for the content of controls in the specified size.
- [class func titleBarFont(ofSize: CGFloat) -> NSFont](nsfont/titlebarfont(ofsize:).md)
  Returns the font used for window title bars, in the specified size.
- [class func paletteFont(ofSize: CGFloat) -> NSFont](nsfont/palettefont(ofsize:).md)
  Returns the font used for palette window title bars, in the specified size.
- [class func toolTipsFont(ofSize: CGFloat) -> NSFont](nsfont/tooltipsfont(ofsize:).md)
  Returns the font used for tool tips labels, in the specified size.
- [class var labelFontSize: CGFloat](nsfont/labelfontsize.md)
  Returns the size of the standard label font.
- [class func systemFontSize(for: NSControl.ControlSize) -> CGFloat](nsfont/systemfontsize(for:).md)
  Returns the font size used for the specified control size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/labelfont(ofsize:))*