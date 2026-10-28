# AVPlayerInterstitialEventRestrictionDefaultPolicy

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Enumeration Case

The default restriction policy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```c
AVPlayerInterstitialEventRestrictionDefaultPolicy
```

## Discussion

By default, an event imposes no restrictions.

## See Also

### Configure
- [static var constrainsSeekingForwardInPrimaryContent: AVPlayerInterstitialEvent.Restrictions](../avplayerinterstitialevent/restrictions-swift.struct/constrainsseekingforwardinprimarycontent.md)
  A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.
- [static var requiresPlaybackAtPreferredRateForAdvancement: AVPlayerInterstitialEvent.Restrictions](../avplayerinterstitialevent/restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement.md)
  A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.
- [AVPlayerInterstitialEventRestrictionNone](./avplayerinterstitialeventrestrictionnone.md)
  A value that indicates no restrictions on playback of primary or interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventrestrictions/avplayerinterstitialeventrestrictiondefaultpolicy)*