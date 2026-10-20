# AttributedString.LocalizationOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init()](./localizationoptions/init%28%29.md)
### Instance Properties
- [var applyReplacementIndexAttribute: Bool](./localizationoptions/applyreplacementindexattribute.md)
- [var concepts: [InflectionConcept]?](./localizationoptions/concepts.md)
  The inflection concepts for achieving automatic grammar agreement during localization.
- [var inflect: Bool](./localizationoptions/inflect.md)
  Whether attributes for automatic grammar agreement and formatting should be processed upon loading the string. Default value is `true`.
- [var replacements: [any CVarArg]?](./localizationoptions/replacements.md)
### Type Methods
- [static func localizedPhraseConcept(String) -> AttributedString.LocalizationOptions](./localizationoptions/localizedphraseconcept%28_%29.md)
- [static func termsOfAddressConcept([TermOfAddress]) -> AttributedString.LocalizationOptions](./localizationoptions/termsofaddressconcept%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/localizationoptions)*