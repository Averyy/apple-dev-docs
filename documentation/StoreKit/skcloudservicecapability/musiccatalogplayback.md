# musicCatalogPlayback

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The device allows playback of Apple Music catalog tracks.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicSubscription from MusicKit.

## Declaration

```swift
static var musicCatalogPlayback: SKCloudServiceCapability { get }
```

```c
SKCloudServiceCapabilityMusicCatalogPlayback
```

## Mentions

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md)

## See Also

### Identifying Cloud Service Capabilities
- [static var musicCatalogSubscriptionEligible: SKCloudServiceCapability](./musiccatalogsubscriptioneligible.md)
  The device allows subscription to the Apple Music catalog.
- [static var addToCloudMusicLibrary: SKCloudServiceCapability](./addtocloudmusiclibrary.md)
  The device allows tracks to be added to the user’s music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecapability/musiccatalogplayback)*