# AVMutableVideoCompositionLayerInstruction

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use [`AVVideoCompositionLayerInstruction.Configuration`](./avvideocompositionlayerinstruction/configuration.md) instead.

## Declaration

```swift
class AVMutableVideoCompositionLayerInstruction
```

```objc
@interface AVMutableVideoCompositionLayerInstruction : AVVideoCompositionLayerInstruction
```

## Topics

### Creating an instruction
- [convenience init(assetTrack: AVAssetTrack)](./avmutablevideocompositionlayerinstruction/init%28assettrack%29.md)
  Creates a new mutable video composition layer instruction for the given track.
### Configuring a track ID
- [var trackID: CMPersistentTrackID](./avmutablevideocompositionlayerinstruction/trackid.md)
  The track identifier of the source track to which the compositor applies the instruction.
### Managing properties
- [func setOpacity(Float, at: CMTime)](./avmutablevideocompositionlayerinstruction/setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](./avmutablevideocompositionlayerinstruction/setopacityramp%28fromstartopacity,toendopacity,timerange%29.md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransform(CGAffineTransform, at: CMTime)](./avmutablevideocompositionlayerinstruction/settransform%28_,at%29.md)
  Sets the transform value at a time within the time range of the instruction.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](./avmutablevideocompositionlayerinstruction/settransformramp%28fromstart,toend,timerange%29.md)
  Sets a transform ramp to apply during a given time range.
### Setting crop rectangle values
- [func setCropRectangle(CGRect, at: CMTime)](./avmutablevideocompositionlayerinstruction/setcroprectangle%28_,at%29.md)
  Sets the crop rectangle  value at a time within the time range of the instruction.
- [func setCropRectangleRamp(fromStartCropRectangle: CGRect, toEndCropRectangle: CGRect, timeRange: CMTimeRange)](./avmutablevideocompositionlayerinstruction/setcroprectangleramp%28fromstartcroprectangle,toendcroprectangle,timerange%29.md)
  Sets a crop rectangle ramp to apply during the specified time range.

## Relationships

### Inherits From
- [AVVideoCompositionLayerInstruction](./avvideocompositionlayerinstruction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Built-in video compositing
- [Editing and playing HDR video](./editing-and-playing-hdr-video.md)
  Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](./debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md)
  Resolve common problems when creating compositions, video compositions, and audio mixes.
- [class AVVideoComposition](./avvideocomposition.md)
  An object that describes how to compose video frames at particular points in time.
- [class AVVideoCompositionInstruction](./avvideocompositioninstruction-swift.class.md)
  An operation that a compositor performs.
- [class AVVideoCompositionLayerInstruction](./avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [class AVMutableVideoComposition](./avmutablevideocomposition.md)
  A mutable video composition subclass.
- [class AVMutableVideoCompositionInstruction](./avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction)*