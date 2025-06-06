# CTFontCreateWithPlatformFont(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Creates a new font reference from an ATS font reference.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CTFontCreateWithPlatformFont(_ platformFont: ATSFontRef, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont?
```

#### Return Value

A new font reference for an [`ATSFontRef`](atsfontref.md) with the specified size, matrix, and additional attributes.

## Parameters

- `platformFont`: A valid   object.
- `size`: The point size for the font reference. If   is specified the default font size of 12.0 is used.
- `matrix`: The transformation matrix for the font.  In most cases, set this parameter to be  .  If  , the identity matrix is used. Optional.
- `attributes`: A   containing additional attributes that should be matched. Optional.

## See Also

- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](ctfontcopygraphicsfont(_:_:).md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](ctfontcreatewithgraphicsfont(_:_:_:_:).md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](ctfontgetplatformfont(_:_:).md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](ctfontcreatewithquickdrawinstance(_:_:_:_:).md)
  Returns a font reference for the given QuickDraw instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithplatformfont(_:_:_:_:))*