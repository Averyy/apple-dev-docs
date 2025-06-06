# userFixedPitchFont(ofSize:)

**Framework**: AppKit  
**Kind**: method

Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), when that font should be fixed-pitch, in the specified size.

**Availability**:
- macOS ?+

## Declaration

```swift
class func userFixedPitchFont(ofSize fontSize: CGFloat) -> NSFont?
```

#### Return Value

A font object of the specified size.

#### Discussion

If `fontSize` is 0 or negative, returns the fixed-pitch font at the default size.

The system does not guarantee that all the glyphs in a fixed-pitch font are the same width. For example, certain Japanese fonts are dual-pitch, and other fonts may have nonspacing marks that can affect the display of other glyphs.

## Parameters

- `fontSize`: The size in points to which the font is scaled.

## See Also

- [init?(name: String, size: CGFloat)](nsfont/init(name:size:).md)
  Creates a font object for the specified font name and font size.
- [class func setUserFixedPitch(NSFont?)](nsfont/setuserfixedpitch(_:).md)
  Sets the font used by default for documents and other text under the user’s control, when that font should be fixed-pitch, to the specified font.
- [class func userFont(ofSize: CGFloat) -> NSFont?](nsfont/userfont(ofsize:).md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), in the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/userfixedpitchfont(ofsize:))*