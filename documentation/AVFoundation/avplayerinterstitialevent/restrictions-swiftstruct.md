# AVPlayerInterstitialEvent.Restrictions

**Framework**: AVFoundation  
**Kind**: struct

Constants that define restrictions on the playback of interstitial content.

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
struct Restrictions
```

## Topics

### Configure
- [static var constrainsSeekingForwardInPrimaryContent: AVPlayerInterstitialEvent.Restrictions](avplayerinterstitialevent/restrictions-swift.struct/constrainsseekingforwardinprimarycontent.md)
  A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.
- [static var requiresPlaybackAtPreferredRateForAdvancement: AVPlayerInterstitialEvent.Restrictions](avplayerinterstitialevent/restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement.md)
  A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.
### Initializing a restriction
- [init(rawValue: UInt)](avplayerinterstitialevent/restrictions-swift.struct/init(rawvalue:).md)
  Creates a restriction with an integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var restrictions: AVPlayerInterstitialEvent.Restrictions](avplayerinterstitialevent/restrictions-swift.property.md)
  The restrictions the event imposes on the playback of interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct)*