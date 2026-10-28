# INSpeakableString

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A custom phrase to be resolved by an Intents extension.

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
class INSpeakableString
```

```objc
@interface INSpeakableString : NSObject
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Overview

When creating your Intents extension, you can define custom vocabulary for some types of intents. For example, a workout app may provide a custom `AppIntentVocabulary.plist` file with the names of standard workouts that are shared by all users of the app. In places where those terms might be used, the intent object contains an [`INSpeakableString`](./inspeakablestring.md) object.

Use the contents of an [`INSpeakableString`](./inspeakablestring.md) object to resolve the specified term during the handling of an intent. If the user spoke a term that is defined in your `AppIntentVocabulary.plist` file, Siri includes the identifier of that term in the string’s [`identifier`](./inspeakable/identifier.md) property. For unrecognized terms, the identifier is `nil`.

## Topics

### Initializing a Speakable String
- [convenience init(spokenPhrase: String)](./inspeakablestring/init%28spokenphrase%29.md)
  Initializes the string with the specified phrase.
- [init(vocabularyIdentifier: String, spokenPhrase: String, pronunciationHint: String?)](./inspeakablestring/init%28vocabularyidentifier,spokenphrase,pronunciationhint%29.md)
  Initializes the string with a phrase from your app’s vocabulary.
- [convenience init(identifier: String, spokenPhrase: String, pronunciationHint: String?)](./inspeakablestring/init%28identifier,spokenphrase,pronunciationhint%29.md)
  Initializes the string with the specified identifier and phrase information.
### Initializers
- [init?(coder: NSCoder)](./inspeakablestring/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INSpeakable](./inspeakable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### String
- [protocol INSpeakable](./inspeakable.md)
  Pronunciation hints for strings used in a spoken interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspeakablestring)*