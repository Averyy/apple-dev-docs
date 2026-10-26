# init(identifier:spokenPhrase:pronunciationHint:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the string with the specified identifier and phrase information.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`init(vocabularyIdentifier:spokenPhrase:pronunciationHint:)`](./init%28vocabularyidentifier,spokenphrase,pronunciationhint%29.md) instead.

## Declaration

```swift
convenience init(identifier: String, spokenPhrase: String, pronunciationHint: String?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier spokenPhrase:(NSString *) spokenPhrase pronunciationHint:(NSString *) pronunciationHint;
```

#### Return Value

An initialized speakable string object.

## Parameters

- `identifier`: The identifier associated with the phrase in your Intents extension’s custom vocabulary file.
- `spokenPhrase`: The phrase to be spoken.
- `pronunciationHint`: A hint about how the phrase is pronounced. This string is not a phonetic spelling of the original phrase, but is a string that has an equivalent sound when spoken. For example, the phrase “iTunes” could have “eye toons” as its pronunciation string.

## See Also

### Initializing a Speakable String
- [convenience init(spokenPhrase: String)](./init%28spokenphrase%29.md)
  Initializes the string with the specified phrase.
- [init(vocabularyIdentifier: String, spokenPhrase: String, pronunciationHint: String?)](./init%28vocabularyidentifier,spokenphrase,pronunciationhint%29.md)
  Initializes the string with a phrase from your app’s vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakablestring/init(identifier:spokenphrase:pronunciationhint:))*