# constrainsSeekingForwardInPrimaryContent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.

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
static var constrainsSeekingForwardInPrimaryContent: AVPlayerInterstitialEvent.Restrictions { get }
```

```c
AVPlayerInterstitialEventRestrictionConstrainsSeekingForwardInPrimaryContent
```

## See Also

### Configure
- [static var requiresPlaybackAtPreferredRateForAdvancement: AVPlayerInterstitialEvent.Restrictions](./requiresplaybackatpreferredrateforadvancement.md)
  A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.
- [AVPlayerInterstitialEventRestrictionDefaultPolicy](../../avplayerinterstitialeventrestrictions/avplayerinterstitialeventrestrictiondefaultpolicy.md)
  The default restriction policy.
- [AVPlayerInterstitialEventRestrictionNone](../../avplayerinterstitialeventrestrictions/avplayerinterstitialeventrestrictionnone.md)
  A value that indicates no restrictions on playback of primary or interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct/constrainsseekingforwardinprimarycontent)*