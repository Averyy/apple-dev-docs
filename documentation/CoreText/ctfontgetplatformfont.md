# CTFontGetPlatformFont(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns an ATS font reference and attributes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CTFontGetPlatformFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef
```

#### Return Value

An [`ATSFontRef`](atsfontref.md) object for the given font reference.

## Parameters

- `font`: The font reference.
- `attributes`: On output, points to a font descriptor containing additional attributes from the font. Can be  . Must be released by the caller.

## See Also

- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](ctfontcopygraphicsfont(_:_:).md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](ctfontcreatewithgraphicsfont(_:_:_:_:).md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](ctfontcreatewithplatformfont(_:_:_:_:).md)
  Creates a new font reference from an ATS font reference.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](ctfontcreatewithquickdrawinstance(_:_:_:_:).md)
  Returns a font reference for the given QuickDraw instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetplatformfont(_:_:))*