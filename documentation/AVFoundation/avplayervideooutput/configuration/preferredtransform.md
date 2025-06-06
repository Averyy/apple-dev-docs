# preferredTransform

**Framework**: AVFoundation  
**Kind**: property

The preferred transform of the visual media.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var preferredTransform: CGAffineTransform { get }
```

#### Discussion

The system retrieves the transform from the [`AVAssetTrack`](avassettrack.md) that provides the media data. If the source track doesn’t specify a transform, the value of this property is [`CGAffineTransformIdentity`](https://developer.apple.com/documentation/CoreGraphics/CGAffineTransformIdentity).

## See Also

- [var sourcePlayerItem: AVPlayerItem?](avplayervideooutput/configuration/sourceplayeritem.md)
  The player item that’s the source of this configuration.
- [var dataChannelDescription: [[CMTag]]](avplayervideooutput/configuration/datachanneldescription.md)
  An array of data channels selected for this configuration.
- [var activationTime: CMTime](avplayervideooutput/configuration/activationtime.md)
  The host time this configuration became active on its associated player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/configuration/preferredtransform)*