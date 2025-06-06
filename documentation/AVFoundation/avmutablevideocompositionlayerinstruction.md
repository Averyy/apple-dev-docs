# AVMutableVideoCompositionLayerInstruction

**Framework**: AVFoundation  
**Kind**: class

An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVMutableVideoCompositionLayerInstruction
```

## Topics

### Creating an Instruction
- [convenience init(assetTrack: AVAssetTrack)](avmutablevideocompositionlayerinstruction/init(assettrack:).md)
  Creates a new mutable video composition layer instruction for the given track.
### Configuring a Track ID
- [var trackID: CMPersistentTrackID](avmutablevideocompositionlayerinstruction/trackid.md)
  The track identifier of the source track to which the compositor applies the instruction.
### Managing Properties
- [func setOpacity(Float, at: CMTime)](avmutablevideocompositionlayerinstruction/setopacity(_:at:).md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:).md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransform(CGAffineTransform, at: CMTime)](avmutablevideocompositionlayerinstruction/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:).md)
  Sets a transform ramp to apply during a given time range.
### Setting Crop Rectangle Values
- [func setCropRectangle(CGRect, at: CMTime)](avmutablevideocompositionlayerinstruction/setcroprectangle(_:at:).md)
  Sets the crop rectangle  value at a time within the time range of the instruction.
- [func setCropRectangleRamp(fromStartCropRectangle: CGRect, toEndCropRectangle: CGRect, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/setcroprectangleramp(fromstartcroprectangle:toendcroprectangle:timerange:).md)
  Sets a crop rectangle ramp to apply during the specified time range.

## Relationships

### Inherits From
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Editing and Playing HDR Video](editing-and-playing-hdr-video.md)
  Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md)
  Resolve common problems when creating compositions, video compositions, and audio mixes.
- [class AVVideoComposition](avvideocomposition.md)
  An object that describes how to compose video frames at particular points in time.
- [class AVMutableVideoComposition](avmutablevideocomposition.md)
  A mutable video composition subclass.
- [class AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)
  An operation that a compositor performs.
- [class AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.
- [class AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction)*