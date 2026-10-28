# init(spokenPhrase:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the string with the specified phrase.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.1+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
convenience init(spokenPhrase: String)
```

```objc
- (instancetype) initWithSpokenPhrase:(NSString *) spokenPhrase;
```

## Return Value

An initialized speakable string object.

## Parameters

- `spokenPhrase`: The phrase to be spoken.

## See Also

### Initializing a Speakable String
- [init(vocabularyIdentifier: String, spokenPhrase: String, pronunciationHint: String?)](./init%28vocabularyidentifier,spokenphrase,pronunciationhint%29.md)
  Initializes the string with a phrase from your app’s vocabulary.
- [convenience init(identifier: String, spokenPhrase: String, pronunciationHint: String?)](./init%28identifier,spokenphrase,pronunciationhint%29.md)
  Initializes the string with the specified identifier and phrase information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakablestring/init(spokenphrase:))*