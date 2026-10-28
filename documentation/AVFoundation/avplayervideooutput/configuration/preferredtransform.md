# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CGAffineTransform preferredTransform;
```

## Discussion

The system retrieves the transform from the [`AVAssetTrack`](../../avassettrack.md) that provides the media data. If the source track doesn’t specify a transform, the value of this property is [`CGAffineTransformIdentity`](../../../CoreGraphics/cgaffinetransformidentity.md).

## See Also

### Inspecting the configuration
- [var sourcePlayerItem: AVPlayerItem?](./sourceplayeritem.md)
  The player item that’s the source of this configuration.
- [var dataChannelDescription: [[CMTag]]](./datachanneldescription.md)
  An array of data channels selected for this configuration.
- [var activationTime: CMTime](./activationtime.md)
  The host time this configuration became active on its associated player object.
- [dataChannelDescriptions](../../avplayervideooutputconfiguration/datachanneldescriptions.md)
  An array of data channels selected for this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/configuration/preferredtransform)*