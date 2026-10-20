# userFont(ofSize:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), in the specified size.

**Availability**:
- macOS

## Declaration

```swift
class func userFont(ofSize fontSize: CGFloat) -> NSFont?
```

```objc
+ (NSFont *) userFontOfSize:(CGFloat) fontSize;
```

#### Return Value

A font object of the specified size.

#### Discussion

If `fontSize` is 0 or negative, returns the user font at the default size.

## Parameters

- `fontSize`: The size in points to which the font is scaled.

## See Also

### Related Documentation
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates a font object for the specified font name and font size.
- [class func setUser(NSFont?)](./setuser%28_%29.md)
  Sets the font used by default for documents and other text under the user’s control to the specified font.
### Creating User Fonts
- [class func userFixedPitchFont(ofSize: CGFloat) -> NSFont?](./userfixedpitchfont%28ofsize%29.md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), when that font should be fixed-pitch, in the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/userfont(ofsize:))*