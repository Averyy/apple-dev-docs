# AVVideoCompositionLayerInstruction

**Framework**: AVFoundation  
**Kind**: class

An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVVideoCompositionLayerInstruction
```

## Topics

### Creating a layer instruction
- [convenience init(configuration: AVVideoCompositionLayerInstruction.Configuration)](avvideocompositionlayerinstruction/init(configuration:).md)
  Initialize an AVVideoCompositionLayerInstruction with a configuration.
- [AVVideoCompositionLayerInstruction.Configuration](avvideocompositionlayerinstruction/configuration.md)
  Configurable properties for initializing a new AVVideoCompositionLayerInstruction instance.
### Getting the track ID
- [var trackID: CMPersistentTrackID](avvideocompositionlayerinstruction/trackid.md)
  The track identifier of the source track to which the compositor will apply the instruction.
### Getting opacity, transform, and cropping ramps
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [AVVideoCompositionLayerInstruction.CropRectangleRamp](avvideocompositionlayerinstruction/croprectangleramp.md)
- [func getCropRectangleRamp(for: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](avvideocompositionlayerinstruction/opacityramp(at:).md)
  Obtains the opacity ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.OpacityRamp](avvideocompositionlayerinstruction/opacityramp.md)
- [func getOpacityRamp(for: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/getopacityramp(for:startopacity:endopacity:timerange:).md)
  Obtains the opacity ramp that includes a specified time.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.
- [AVVideoCompositionLayerInstruction.TransformRamp](avvideocompositionlayerinstruction/transformramp.md)
- [func getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:).md)
  Obtains the transform ramp that includes a specified time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Editing and playing HDR video](editing-and-playing-hdr-video.md)
  Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md)
  Resolve common problems when creating compositions, video compositions, and audio mixes.
- [class AVVideoComposition](avvideocomposition.md)
  An object that describes how to compose video frames at particular points in time.
- [class AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)
  An operation that a compositor performs.
- [class AVMutableVideoComposition](avmutablevideocomposition.md)
  A mutable video composition subclass.
- [class AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.
- [class AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction)*