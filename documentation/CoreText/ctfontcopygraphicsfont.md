# CTFontCopyGraphicsFont(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a Core Graphics font reference and attributes.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCopyGraphicsFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont
```

#### Return Value

A [`CGFont`](https://developer.apple.com/documentation/CoreGraphics/CGFont) object for the given font reference.

## Parameters

- `font`: The font reference.
- `attributes`: On output, points to a font descriptor containing additional attributes from the font. Can be  . Must be released by the caller.

## See Also

- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](ctfontcreatewithgraphicsfont(_:_:_:_:).md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](ctfontgetplatformfont(_:_:).md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](ctfontcreatewithplatformfont(_:_:_:_:).md)
  Creates a new font reference from an ATS font reference.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](ctfontcreatewithquickdrawinstance(_:_:_:_:).md)
  Returns a font reference for the given QuickDraw instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopygraphicsfont(_:_:))*