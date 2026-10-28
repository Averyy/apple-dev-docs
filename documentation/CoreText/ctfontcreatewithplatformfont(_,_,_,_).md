# CTFontCreateWithPlatformFont(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates a new font reference from an ATS font reference.

**Availability**:
- macOS 10.5+ - Deprecated in 11.0

> **Deprecated**: ATS is deprecated

## Declaration

```swift
func CTFontCreateWithPlatformFont(_ platformFont: ATSFontRef, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont?
```

```c
extern CTFontRefCTFontCreateWithPlatformFont(ATSFontRef platformFont, CGFloat size, const CGAffineTransform *matrix, CTFontDescriptorRef attributes);
```

## Return Value

A new font reference for an [`ATSFontRef`](./atsfontref.md) with the specified size, matrix, and additional attributes.

## Parameters

- `platformFont`: A valid [`ATSFontRef`](./atsfontref.md) object.
- `size`: The point size for the font reference. If `0.0` is specified the default font size of 12.0 is used.
- `matrix`: The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL`, the identity matrix is used. Optional.
- `attributes`: A [`CTFontDescriptor`](./ctfontdescriptor.md) containing additional attributes that should be matched. Optional.

## See Also

### Converting Fonts
- [func CTFontCopyGraphicsFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](./ctfontcopygraphicsfont%28_,_%29.md)
  Returns a Core Graphics font reference and attributes.
- [func CTFontCreateWithGraphicsFont(CGFont, CGFloat, UnsafePointer<CGAffineTransform>?, CTFontDescriptor?) -> CTFont](./ctfontcreatewithgraphicsfont%28_,_,_,_%29.md)
  Creates a new font reference from an existing Core Graphics font reference.
- [func CTFontGetPlatformFont(CTFont, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef](./ctfontgetplatformfont%28_,_%29.md)
  Returns an ATS font reference and attributes.
- [func CTFontCreateWithQuickdrawInstance(ConstStr255Param?, Int16, UInt8, CGFloat) -> CTFont](./ctfontcreatewithquickdrawinstance%28_,_,_,_%29.md)
  Returns a font reference for the given QuickDraw instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcreatewithplatformfont(_:_:_:_:))*