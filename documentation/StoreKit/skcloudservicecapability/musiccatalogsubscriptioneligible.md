# musicCatalogSubscriptionEligible

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The device allows subscription to the Apple Music catalog.

**Availability**:
- iOS 10.1+ - Deprecated in 18.0
- iPadOS 10.1+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 10.1+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use the canBecomeSubscriber property of MusicSubscription from MusicKit.

## Declaration

```swift
static var musicCatalogSubscriptionEligible: SKCloudServiceCapability { get }
```

```c
SKCloudServiceCapabilityMusicCatalogSubscriptionEligible
```

## Mentions

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md)

## See Also

### Identifying Cloud Service Capabilities
- [static var musicCatalogPlayback: SKCloudServiceCapability](./musiccatalogplayback.md)
  The device allows playback of Apple Music catalog tracks.
- [static var addToCloudMusicLibrary: SKCloudServiceCapability](./addtocloudmusiclibrary.md)
  The device allows tracks to be added to the user’s music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecapability/musiccatalogsubscriptioneligible)*