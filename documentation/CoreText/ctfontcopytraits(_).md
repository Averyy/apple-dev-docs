# CTFontCopyTraits(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the traits dictionary of the given font.

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
func CTFontCopyTraits(_ font: CTFont) -> CFDictionary
```

```c
extern CFDictionaryRefCTFontCopyTraits(CTFontRef font);
```

## Return Value

A retained reference to the font traits dictionary. Individual traits can be accessed with the trait key constants.

## Discussion

See the Constants section of [`CTFontDescriptor`](./ctfontdescriptor.md) for a definition of the font traits.

## Parameters

- `font`: The font reference.

## See Also

### Getting Font Data
- [func CTFontCopyFontDescriptor(CTFont) -> CTFontDescriptor](./ctfontcopyfontdescriptor%28_%29.md)
  Returns the normalized font descriptor for the given font reference.
- [func CTFontCopyAttribute(CTFont, CFString) -> CFTypeRef?](./ctfontcopyattribute%28_,_%29.md)
  Returns the value associated with an arbitrary attribute of the given font.
- [func CTFontGetSize(CTFont) -> CGFloat](./ctfontgetsize%28_%29.md)
  Returns the point size of the given font.
- [func CTFontGetMatrix(CTFont) -> CGAffineTransform](./ctfontgetmatrix%28_%29.md)
  Returns the transformation matrix of the given font.
- [func CTFontGetSymbolicTraits(CTFont) -> CTFontSymbolicTraits](./ctfontgetsymbolictraits%28_%29.md)
  Returns the symbolic traits of the given font.
- [func CTFontCopyDefaultCascadeListForLanguages(CTFont, CFArray?) -> CFArray?](./ctfontcopydefaultcascadelistforlanguages%28_,_%29.md)
  Retrieves an ordered list of font substitution preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopytraits(_:))*