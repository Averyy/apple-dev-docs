# init(vocabularyIdentifier:spokenPhrase:pronunciationHint:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the string with a phrase from your app’s vocabulary.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(vocabularyIdentifier: String, spokenPhrase: String, pronunciationHint: String?)
```

```objc
- (instancetype) initWithVocabularyIdentifier:(NSString *) vocabularyIdentifier spokenPhrase:(NSString *) spokenPhrase pronunciationHint:(NSString *) pronunciationHint;
```

## Return Value

An initialized speakable string object.

## Parameters

- `vocabularyIdentifier`: The identifier of a phrase that your app registered as part of its vocabulary.
- `spokenPhrase`: The spoken phrase associated with that vocabulary.
- `pronunciationHint`: A hint at how the spoken phrase is pronounced. This string is not a phonetic spelling of the original phrase, but is a string that has an equivalent sound when spoken. For example, the phrase “iTunes” could have “eye toons” as its pronunciation string.

## See Also

### Initializing a Speakable String
- [convenience init(spokenPhrase: String)](./init%28spokenphrase%29.md)
  Initializes the string with the specified phrase.
- [convenience init(identifier: String, spokenPhrase: String, pronunciationHint: String?)](./init%28identifier,spokenphrase,pronunciationhint%29.md)
  Initializes the string with the specified identifier and phrase information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakablestring/init(vocabularyidentifier:spokenphrase:pronunciationhint:))*