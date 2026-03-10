# kCTFontDescriptorLanguageAttribute

**Framework**: Core Text  
**Kind**: var

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCTFontDescriptorLanguageAttribute: CFString
```

#### Discussion

The language identifier for font fallback selection.

The value associated with this key is a CFStringRef. If specified in a font descriptor, it is used to select the appropriate font fallback list for the language. This key should not be confused with kCTLanguageAttributeName, which is defined in CTStringAttributes.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontdescriptorlanguageattribute)*