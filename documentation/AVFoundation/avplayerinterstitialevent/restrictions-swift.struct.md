# AVPlayerInterstitialEvent.Restrictions

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVPlayerInterstitialEventRestrictions : NSUInteger;
```

## Topics

### Configure
- [static var constrainsSeekingForwardInPrimaryContent: AVPlayerInterstitialEvent.Restrictions](./restrictions-swift.struct/constrainsseekingforwardinprimarycontent.md)
  A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.
- [static var requiresPlaybackAtPreferredRateForAdvancement: AVPlayerInterstitialEvent.Restrictions](./restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement.md)
  A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.
### Initializing a restriction
- [init(rawValue: UInt)](./restrictions-swift.struct/init%28rawvalue%29.md)
  Creates a restriction with an integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing restrictions
- [var restrictions: AVPlayerInterstitialEvent.Restrictions](./restrictions-swift.property.md)
  The restrictions the event imposes on the playback of interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct)*