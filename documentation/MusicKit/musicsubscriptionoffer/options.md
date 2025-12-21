# MusicSubscriptionOffer.Options

**Framework**: MusicKit  
**Kind**: struct

Options for loading subscription offers for Apple Music.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Options
```

## Topics

### Initializers
- [init(action: MusicSubscriptionOffer.Action, messageIdentifier: MusicSubscriptionOffer.MessageIdentifier, itemID: MusicItemID?, affiliateToken: String?, campaignToken: String?)](musicsubscriptionoffer/options/init(action:messageidentifier:itemid:affiliatetoken:campaigntoken:).md)
  Creates options for a subscription offer sheet with specific values for common properties.
### Instance Properties
- [var action: MusicSubscriptionOffer.Action](musicsubscriptionoffer/options/action.md)
  An action for the subscription offers entry point.
- [var affiliateToken: String?](musicsubscriptionoffer/options/affiliatetoken.md)
  An affiliate token for the Apple Services affiliate program.
- [var campaignToken: String?](musicsubscriptionoffer/options/campaigntoken.md)
  A campaign token for the Apple Services affiliate program.
- [var itemID: MusicItemID?](musicsubscriptionoffer/options/itemid.md)
  An identifier for the music item the user is trying to access, which requires an active subscription.
- [var messageIdentifier: MusicSubscriptionOffer.MessageIdentifier](musicsubscriptionoffer/options/messageidentifier.md)
  An identifier for selecting the main message that the subscription offer sheet presents to the user.
### Type Properties
- [static let `default`: MusicSubscriptionOffer.Options](musicsubscriptionoffer/options/default.md)
  The default set of options for loading subscription offers for Apple Music.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/options)*