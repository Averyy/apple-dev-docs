# MusicSubscriptionOffer.MessageIdentifier

**Framework**: MusicKit  
**Kind**: struct

An identifier for the main message that the subscription offer sheet presents to the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct MessageIdentifier
```

## Topics

### Initializers
- [init(String)](musicsubscriptionoffer/messageidentifier/init(_:).md)
  Creates a message identifier with the specified raw value.
- [init(rawValue: String)](musicsubscriptionoffer/messageidentifier/init(rawvalue:).md)
  Creates a message identifier with the specified raw value.
### Instance Properties
- [let rawValue: String](musicsubscriptionoffer/messageidentifier/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [MusicSubscriptionOffer.MessageIdentifier.RawValue](musicsubscriptionoffer/messageidentifier/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let addMusic: MusicSubscriptionOffer.MessageIdentifier](musicsubscriptionoffer/messageidentifier/addmusic.md)
  An identifier for the message that invites the user to add music to their library by subscribing to Apple Music.
- [static let join: MusicSubscriptionOffer.MessageIdentifier](musicsubscriptionoffer/messageidentifier/join.md)
  An identifier for the message that invites the user to join Apple Music.
- [static let playMusic: MusicSubscriptionOffer.MessageIdentifier](musicsubscriptionoffer/messageidentifier/playmusic.md)
  An identifier for the message that invites the user to play music by subscribing to Apple Music.
### Default Implementations
- [CustomStringConvertible Implementations](musicsubscriptionoffer/messageidentifier/customstringconvertible-implementations.md)
- [Equatable Implementations](musicsubscriptionoffer/messageidentifier/equatable-implementations.md)
- [RawRepresentable Implementations](musicsubscriptionoffer/messageidentifier/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/messageidentifier)*