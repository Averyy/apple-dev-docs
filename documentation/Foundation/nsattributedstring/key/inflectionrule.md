# inflectionRule

**Framework**: Foundation  
**Kind**: property

An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let inflectionRule: NSAttributedString.Key
```

#### Discussion

The value of this key is an [`NSInflectionRule`](nsinflectionrule.md) object.

## See Also

- [static let languageIdentifier: NSAttributedString.Key](nsattributedstring/key/languageidentifier.md)
  The language identifier associated with the range of text.
- [static let morphology: NSAttributedString.Key](nsattributedstring/key/morphology.md)
  An attribute that contains grammatical properties to apply to the text.
- [static let inflectionAlternative: NSAttributedString.Key](nsattributedstring/key/inflectionalternative.md)
  The alternative translation for a string when no suitable inflection exists.
- [static let agreeWithArgument: NSAttributedString.Key](nsattributedstring/key/agreewithargument.md)
- [static let agreeWithConcept: NSAttributedString.Key](nsattributedstring/key/agreewithconcept.md)
- [static let referentConcept: NSAttributedString.Key](nsattributedstring/key/referentconcept.md)
- [static let localizedNumberFormat: NSAttributedString.Key](nsattributedstring/key/localizednumberformat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/inflectionrule)*