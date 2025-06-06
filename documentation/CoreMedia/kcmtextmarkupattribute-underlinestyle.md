# kCMTextMarkupAttribute_UnderlineStyle

**Framework**: Core Media  
**Kind**: var

An underline font style.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMTextMarkupAttribute_UnderlineStyle: CFString
```

#### Discussion

This attribute’s value must be a `CFBoolean`. The default is `kCFBooleanFalse`. If this attribute is `kCFBooleanTrue`, the system renders the text with an underline style in addition to other styles you use.

## See Also

- [let kCMTextMarkupAttribute_BoldStyle: CFString](kcmtextmarkupattribute_boldstyle.md)
  A bold font style.
- [let kCMTextMarkupAttribute_ItalicStyle: CFString](kcmtextmarkupattribute_italicstyle.md)
  An italic font style.
- [let kCMTextMarkupAttribute_CharacterEdgeStyle: CFString](kcmtextmarkupattribute_characteredgestyle.md)
  A style for character edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_underlinestyle)*