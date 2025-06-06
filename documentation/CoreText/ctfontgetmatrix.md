# CTFontGetMatrix(_:)

**Framework**: Core Text  
**Kind**: func

Returns the transformation matrix of the given font.

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
func CTFontGetMatrix(_ font: CTFont) -> CGAffineTransform
```

#### Return Value

The transformation matrix for the given font reference. This is the matrix that was provided when the font was created.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyFontDescriptor(CTFont) -> CTFontDescriptor](ctfontcopyfontdescriptor(_:).md)
  Returns the normalized font descriptor for the given font reference.
- [func CTFontCopyAttribute(CTFont, CFString) -> CFTypeRef?](ctfontcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute of the given font.
- [func CTFontGetSize(CTFont) -> CGFloat](ctfontgetsize(_:).md)
  Returns the point size of the given font.
- [func CTFontGetSymbolicTraits(CTFont) -> CTFontSymbolicTraits](ctfontgetsymbolictraits(_:).md)
  Returns the symbolic traits of the given font.
- [func CTFontCopyTraits(CTFont) -> CFDictionary](ctfontcopytraits(_:).md)
  Returns the traits dictionary of the given font.
- [func CTFontCopyDefaultCascadeListForLanguages(CTFont, CFArray?) -> CFArray?](ctfontcopydefaultcascadelistforlanguages(_:_:).md)
  Retrieves an ordered list of font substitution preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetmatrix(_:))*