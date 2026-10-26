# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The identifier associated with the string in your app’s custom vocabulary file.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`vocabularyIdentifier`](./vocabularyidentifier.md) instead.

## Declaration

```swift
optional var identifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSString * identifier;
```

#### Discussion

For phrases that are included in your app’s `AppIntentVocabulary.plist` file, this property contains the value of the `VocabularyItemIdentifier` key associated with that phrase. When determining the resolution for speakable strings, you can use this identifier (when present) to validate and resolve the term to a known phrase.

If the specified phrase was not defined in your vocabulary file, this property is `nil`.

## See Also

### Getting the Identifier
- [var vocabularyIdentifier: String?](./vocabularyidentifier.md)
  The identifier associated with the string in your app’s custom vocabulary file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakable/identifier)*