# AttributeScopes.TranslationAttributes

**Framework**: Foundation  
**Kind**: struct

A scope that defines translation-specific properties on attributed strings.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct TranslationAttributes
```

#### Overview

Use this scope to access translation attributes when working with [`AttributedString`](attributedstring.md) instances.

## Topics

### Handling translation behavior
- [let skipsTranslation: AttributeScopes.TranslationAttributes.SkipTranslationAttribute](attributescopes/translationattributes/skipstranslation.md)
  An attribute that marks portions of an attributed string to be excluded from translation.
- [AttributeScopes.TranslationAttributes.SkipTranslationAttribute](attributescopes/translationattributes/skiptranslationattribute.md)
  The attribute key for skipping translation.

## Relationships

### Conforms To
- [AttributeScope](attributescope.md)
- [DecodingConfigurationProviding](decodingconfigurationproviding.md)
- [EncodingConfigurationProviding](encodingconfigurationproviding.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var translation: AttributeScopes.TranslationAttributes.Type](attributescopes/translation.md)
  Provides access to translation-related attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/translationattributes)*