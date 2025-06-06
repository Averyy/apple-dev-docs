# inflectionAlternative

**Framework**: Foundation  
**Kind**: property

The alternative translation for a string when no suitable inflection exists.

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
static let inflectionAlternative: NSAttributedString.Key
```

#### Discussion

In languages that change the form of words to match someone’s gender, the system can automatically change (or inflect) the gender to match someone’s personal preferences. If a suitable inflection doesn’t exist, the system uses the value of this attribute instead. Add this attribute to specify a suitable translation that applies to anyone. For example, if a language has only masculine and feminine genders, specify an appropriately neutral translation of the text.

The value of this key is an [`NSString`](nsstring.md) with the replacement phrase to use.

## See Also

- [static let languageIdentifier: NSAttributedString.Key](nsattributedstring/key/languageidentifier.md)
  The language identifier associated with the range of text.
- [static let morphology: NSAttributedString.Key](nsattributedstring/key/morphology.md)
  An attribute that contains grammatical properties to apply to the text.
- [static let inflectionRule: NSAttributedString.Key](nsattributedstring/key/inflectionrule.md)
  An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.
- [static let agreeWithArgument: NSAttributedString.Key](nsattributedstring/key/agreewithargument.md)
- [static let agreeWithConcept: NSAttributedString.Key](nsattributedstring/key/agreewithconcept.md)
- [static let referentConcept: NSAttributedString.Key](nsattributedstring/key/referentconcept.md)
- [static let localizedNumberFormat: NSAttributedString.Key](nsattributedstring/key/localizednumberformat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/inflectionalternative)*