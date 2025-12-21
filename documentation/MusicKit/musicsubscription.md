# MusicSubscription

**Framework**: MusicKit  
**Kind**: struct

A representation of the current state of the user’s subscription to Apple Music.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct MusicSubscription
```

## Topics

### Structures
- [MusicSubscription.Updates](musicsubscription/updates.md)
  An asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.
### Instance Properties
- [let canBecomeSubscriber: Bool](musicsubscription/canbecomesubscriber.md)
  A capability that allows your app to present subscription offers for Apple Music.
- [let canPlayCatalogContent: Bool](musicsubscription/canplaycatalogcontent.md)
  A capability that allows your app to play subscription content using a music player.
- [let hasCloudLibraryEnabled: Bool](musicsubscription/hascloudlibraryenabled.md)
  A capability that allows your app to perform modifications to the user’s iCloud Music Library.
### Type Properties
- [static var current: MusicSubscription](musicsubscription/current.md)
  The current state of the user’s subscription to Apple Music.
- [static var subscriptionUpdates: MusicSubscription.Updates](musicsubscription/subscriptionupdates.md)
  An asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.
### Enumerations
- [MusicSubscription.Error](musicsubscription/error.md)
  An error that MusicKit can throw upon requesting the current music subscription of the user.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MusicSubscriptionOffer](musicsubscriptionoffer.md)
  A type for grouping other types for showing subscription offers for Apple Music.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription)*