# AttributedString.LocalizationOptions

**Framework**: Foundation  
**Kind**: struct

Configuration options for the localization of text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct LocalizationOptions
```

## Topics

### Initializers
- [init()](attributedstring/localizationoptions/init.md)
### Instance Properties
- [var applyReplacementIndexAttribute: Bool](attributedstring/localizationoptions/applyreplacementindexattribute.md)
- [var concepts: [InflectionConcept]?](attributedstring/localizationoptions/concepts.md)
  The inflection concepts for achieving automatic grammar agreement during localization.
- [var inflect: Bool](attributedstring/localizationoptions/inflect.md)
- [var replacements: [any CVarArg]?](attributedstring/localizationoptions/replacements.md)
### Type Methods
- [static func localizedPhraseConcept(String) -> AttributedString.LocalizationOptions](attributedstring/localizationoptions/localizedphraseconcept(_:).md)
- [static func termsOfAddressConcept([TermOfAddress]) -> AttributedString.LocalizationOptions](attributedstring/localizationoptions/termsofaddressconcept(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/localizationoptions)*