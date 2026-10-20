# CTFontCreateWithQuickdrawInstance(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns a font reference for the given QuickDraw instance.

**Availability**:
- macOS 10.5+ - Deprecated in 10.15

> **Deprecated**: Quickdraw font references are deprecated

## Declaration

```swift
func CTFontCreateWithQuickdrawInstance(_ name: ConstStr255Param?, _ identifier: Int16, _ style: UInt8, _ size: CGFloat) -> CTFont
```

```c
extern CTFontRefCTFontCreateWithQuickdrawInstance(ConstStr255Param name, int16_t identifier, uint8_t style, CGFloat size);
```

#### Return Value

The best font instance matching the QuickDraw instance information.

#### Discussion

This function is provided for compatibility support between Core Text and clients needing to support QuickDraw-style font references. QuickDraw is a deprecated technology in macOS 10.4 and later.

## Parameters

- `name`: The QuickDraw font name. If zero length, `identifier` must be specified.
- `identifier`: The QuickDraw font identifier. Can be `0`, but if so, `name` must be specified.
- `style`: The QuickDraw font style.
- `size`: The point size for the font reference. If `0.0` is specified, the default size of 12.0 is used.

## See Also

### Converting Fonts
- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](./ctfontcopygraphicsfont%28_,_%29.md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](./ctfontcreatewithgraphicsfont%28_,_,_,_%29.md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](./ctfontgetplatformfont%28_,_%29.md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](./ctfontcreatewithplatformfont%28_,_,_,_%29.md)
  Creates a new font reference from an ATS font reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithquickdrawinstance(_:_:_:_:))*