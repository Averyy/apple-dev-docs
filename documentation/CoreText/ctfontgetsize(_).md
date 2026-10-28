# CTFontGetSize(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the point size of the given font.

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
func CTFontGetSize(_ font: CTFont) -> CGFloat
```

```c
extern CGFloat CTFontGetSize(CTFontRef font);
```

## Return Value

The point size of the given font reference. This is the point size provided when the font was created.

## Parameters

- `font`: The font reference.

## See Also

### Getting Font Data
- [func CTFontCopyFontDescriptor(CTFont) -> CTFontDescriptor](./ctfontcopyfontdescriptor%28_%29.md)
  Returns the normalized font descriptor for the given font reference.
- [func CTFontCopyAttribute(CTFont, CFString) -> CFTypeRef?](./ctfontcopyattribute%28_,_%29.md)
  Returns the value associated with an arbitrary attribute of the given font.
- [func CTFontGetMatrix(CTFont) -> CGAffineTransform](./ctfontgetmatrix%28_%29.md)
  Returns the transformation matrix of the given font.
- [func CTFontGetSymbolicTraits(CTFont) -> CTFontSymbolicTraits](./ctfontgetsymbolictraits%28_%29.md)
  Returns the symbolic traits of the given font.
- [func CTFontCopyTraits(CTFont) -> CFDictionary](./ctfontcopytraits%28_%29.md)
  Returns the traits dictionary of the given font.
- [func CTFontCopyDefaultCascadeListForLanguages(CTFont, CFArray?) -> CFArray?](./ctfontcopydefaultcascadelistforlanguages%28_,_%29.md)
  Retrieves an ordered list of font substitution preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetsize(_:))*