# INSpeakable

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

Pronunciation hints for strings used in a spoken interface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INSpeakable : NSObjectProtocol
```

```objc
@protocol INSpeakable <NSObject>
```

#### Overview

The [`INSpeakable`](./inspeakable.md) protocol is adopted by the [`INSpeakableString`](./inspeakablestring.md) class and used to provide pronunciation hints for strings spoken by Siri. You do not need to adopt this protocol in your own classes. Instead, create instances of the [`INSpeakableString`](./inspeakablestring.md) class and use them when resolving parameters in your intent handlers.

## Topics

### Getting the Spoken Attributes
- [var spokenPhrase: String](./inspeakable/spokenphrase.md)
  The phrase identified by Siri.
- [var pronunciationHint: String?](./inspeakable/pronunciationhint.md)
  A hint at how the spoken phrase is pronounced.
### Getting the Identifier
- [var vocabularyIdentifier: String?](./inspeakable/vocabularyidentifier.md)
  The identifier associated with the string in your app’s custom vocabulary file.
- [var identifier: String?](./inspeakable/identifier.md)
  The identifier associated with the string in your app’s custom vocabulary file.
### Getting Alternative Matches
- [var alternativeSpeakableMatches: [any INSpeakable]?](./inspeakable/alternativespeakablematches.md)
  An array of alternative phrases that match the current phrase.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [INObject](./inobject.md)
- [INPerson](./inperson.md)
- [INRestaurantGuest](./inrestaurantguest.md)
- [INRideDriver](./inridedriver.md)
- [INSpeakableString](./inspeakablestring.md)

## See Also

### String
- [class INSpeakableString](./inspeakablestring.md)
  A custom phrase to be resolved by an Intents extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakable)*