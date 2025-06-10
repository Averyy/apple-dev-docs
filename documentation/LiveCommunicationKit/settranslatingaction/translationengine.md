# SetTranslatingAction.TranslationEngine

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that describe the translation engine that provided a translation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum TranslationEngine
```

## Topics

### Types
- [SetTranslatingAction.TranslationEngine.default](settranslatingaction/translationengine/default.md)
  The translation was provided by the system’s default translation engine.
- [SetTranslatingAction.TranslationEngine.external](settranslatingaction/translationengine/external.md)
  The translation was provided by an external translation engine.
### Operators
- [static func == (SetTranslatingAction.TranslationEngine, SetTranslatingAction.TranslationEngine) -> Bool](settranslatingaction/translationengine/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](settranslatingaction/translationengine/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](settranslatingaction/translationengine/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](settranslatingaction/translationengine/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func fulfill(using: SetTranslatingAction.TranslationEngine)](settranslatingaction/fulfill(using:).md)
  Reports that the translation action was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/settranslatingaction/translationengine)*