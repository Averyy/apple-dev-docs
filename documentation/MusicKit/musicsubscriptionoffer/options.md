# MusicSubscriptionOffer.Options

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

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
- [init(action: MusicSubscriptionOffer.Action, messageIdentifier: MusicSubscriptionOffer.MessageIdentifier, itemID: MusicItemID?, affiliateToken: String?, campaignToken: String?)](./options/init%28action,messageidentifier,itemid,affiliatetoken,campaigntoken%29.md)
  Creates options for a subscription offer sheet with specific values for common properties.
### Instance Properties
- [var action: MusicSubscriptionOffer.Action](./options/action.md)
  An action for the subscription offers entry point.
- [var affiliateToken: String?](./options/affiliatetoken.md)
  An affiliate token for the Apple Services affiliate program.
- [var campaignToken: String?](./options/campaigntoken.md)
  A campaign token for the Apple Services affiliate program.
- [var itemID: MusicItemID?](./options/itemid.md)
  An identifier for the music item the user is trying to access, which requires an active subscription.
- [var messageIdentifier: MusicSubscriptionOffer.MessageIdentifier](./options/messageidentifier.md)
  An identifier for selecting the main message that the subscription offer sheet presents to the user.
### Type Properties
- [static let `default`: MusicSubscriptionOffer.Options](./options/default.md)
  The default set of options for loading subscription offers for Apple Music.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/options)*