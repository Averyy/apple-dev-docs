# CTFontCreateWithGraphicsFont(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Creates a new font reference from an existing Core Graphics font reference.

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
func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont
```

#### Return Value

A new font reference for an existing [`CGFont`](https://developer.apple.com/documentation/CoreGraphics/CGFont) object with the specified size, matrix, and additional attributes.

## Parameters

- `graphicsFont`: A valid Core Graphics font reference.
- `size`: The point size for the font reference. If   is specified the default font size of 12.0 is used.
- `matrix`: The transformation matrix for the font.  In most cases, set this parameter to be  .  If  , the identity matrix is used. Optional.
- `attributes`: Additional attributes that should be matched. Optional.

## See Also

- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](ctfontcopygraphicsfont(_:_:).md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](ctfontgetplatformfont(_:_:).md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](ctfontcreatewithplatformfont(_:_:_:_:).md)
  Creates a new font reference from an ATS font reference.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](ctfontcreatewithquickdrawinstance(_:_:_:_:).md)
  Returns a font reference for the given QuickDraw instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithgraphicsfont(_:_:_:_:))*