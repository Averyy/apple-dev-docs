# CTFontGetPlatformFont(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns an ATS font reference and attributes.

**Availability**:
- macOS 10.5+ - Deprecated in 11.0

> **Deprecated**: ATS is deprecated

## Declaration

```swift
func CTFontGetPlatformFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef
```

```c
extern ATSFontRef CTFontGetPlatformFont(CTFontRef font, CTFontDescriptorRef*attributes);
```

#### Return Value

An [`ATSFontRef`](./atsfontref.md) object for the given font reference.

## Parameters

- `font`: The font reference.
- `attributes`: On output, points to a font descriptor containing additional attributes from the font. Can be `NULL`. Must be released by the caller.

## See Also

### Converting Fonts
- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](./ctfontcopygraphicsfont%28_,_%29.md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](./ctfontcreatewithgraphicsfont%28_,_,_,_%29.md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont?](./ctfontcreatewithplatformfont%28_,_,_,_%29.md)
  Creates a new font reference from an ATS font reference.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](./ctfontcreatewithquickdrawinstance%28_,_,_,_%29.md)
  Returns a font reference for the given QuickDraw instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetplatformfont(_:_:))*