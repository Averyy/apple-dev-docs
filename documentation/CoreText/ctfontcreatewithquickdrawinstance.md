# CTFontCreateWithQuickdrawInstance(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a font reference for the given QuickDraw instance.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CTFontCreateWithQuickdrawInstance(_ name: ConstStr255Param?, _ identifier: Int16, _ style: UInt8, _ size: CGFloat) -> CTFont
```

#### Return Value

The best font instance matching the QuickDraw instance information.

#### Discussion

This function is provided for compatibility support between Core Text and clients needing to support QuickDraw-style font references. QuickDraw is a deprecated technology in macOS 10.4 and later.

## Parameters

- `name`: The QuickDraw font name. If zero length,   must be specified.
- `identifier`: The QuickDraw font identifier. Can be  , but if so,   must be specified.
- `style`: The QuickDraw font style.
- `size`: The point size for the font reference. If   is specified, the default size of 12.0 is used.

## See Also

- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](ctfontcopygraphicsfont(_:_:).md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](ctfontcreatewithgraphicsfont(_:_:_:_:).md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](ctfontgetplatformfont(_:_:).md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](ctfontcreatewithplatformfont(_:_:_:_:).md)
  Creates a new font reference from an ATS font reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithquickdrawinstance(_:_:_:_:))*