# CTFontCopyAttribute(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns the value associated with an arbitrary attribute of the given font.

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
func CTFontCopyAttribute(_ font: CTFont, _ attribute: CFString) -> CFTypeRef?
```

#### Return Value

A retained reference to an arbitrary attribute or `NULL` if the requested attribute is not present.

#### Discussion

Refer to the attribute definitions documentation for information as to how each attribute is packaged as a `CFType`.

## Parameters

- `font`: The font reference.
- `attribute`: The requested attribute.

## See Also

- [func CTFontCopyFontDescriptor(CTFont) -> CTFontDescriptor](ctfontcopyfontdescriptor(_:).md)
  Returns the normalized font descriptor for the given font reference.
- [func CTFontGetSize(CTFont) -> CGFloat](ctfontgetsize(_:).md)
  Returns the point size of the given font.
- [func CTFontGetMatrix(CTFont) -> CGAffineTransform](ctfontgetmatrix(_:).md)
  Returns the transformation matrix of the given font.
- [func CTFontGetSymbolicTraits(CTFont) -> CTFontSymbolicTraits](ctfontgetsymbolictraits(_:).md)
  Returns the symbolic traits of the given font.
- [func CTFontCopyTraits(CTFont) -> CFDictionary](ctfontcopytraits(_:).md)
  Returns the traits dictionary of the given font.
- [func CTFontCopyDefaultCascadeListForLanguages(CTFont, CFArray?) -> CFArray?](ctfontcopydefaultcascadelistforlanguages(_:_:).md)
  Retrieves an ordered list of font substitution preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyattribute(_:_:))*