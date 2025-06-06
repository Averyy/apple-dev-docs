# AVMutableVideoComposition

**Framework**: AVFoundation  
**Kind**: class

A mutable video composition subclass.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVMutableVideoComposition
```

#### Overview

If you use the built-in video compositor, the instructions a video composition contain can specify a spatial transformation, an opacity value, and a cropping rectangle for each video source. This values can vary over time by applying linear ramping functions.

You can create a custom video compositor by implementing the [`AVVideoCompositing`](avvideocompositing.md) protocol. The system provides the custom video compositor with pixel buffers for each of its video sources during playback, and can perform arbitrary graphical operations on them to produce visual output.

## Topics

### Creating a Video Composition
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [class func videoComposition(withPropertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:).md)
  Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVMutableVideoComposition?, (any Error)?) -> Void)](avmutablevideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [init(propertiesOf: AVAsset)](avmutablevideocomposition/init(propertiesof:).md)
  Creates a mutable video composition with the specified asset properties.
- [init(propertiesOf: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)](avmutablevideocomposition/init(propertiesof:prototypeinstruction:).md)
  Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avmutablevideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.
### Configuring Video Composition Properties
- [var frameDuration: CMTime](avmutablevideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderSize: CGSize](avmutablevideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](avmutablevideocomposition/renderscale.md)
  The scale at which the video composition should render.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](avmutablevideocomposition/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
### Specifying composition instructions
- [var instructions: [any AVVideoCompositionInstructionProtocol]](avmutablevideocomposition/instructions.md)
  The video composition instructions.
- [protocol AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md)
  A protocol that defines the interface for a video composition instruction.
### Configuring HDR Metadata
- [var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avmutablevideocomposition/perframehdrdisplaymetadatapolicy.md)
  Configures the policy for display of HDR display metadata on the rendered frame.
- [AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct.md)
  A type that defines the policy for handling of per frame HDR metadata.
### Configuring Color
- [var colorPrimaries: String?](avmutablevideocomposition/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](avmutablevideocomposition/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](avmutablevideocomposition/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
### Identifying Source Tracks
- [var sourceTrackIDForFrameTiming: CMPersistentTrackID](avmutablevideocomposition/sourcetrackidforframetiming.md)
  An identifier of the source track from which the video composition derives frame timing.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](avmutablevideocomposition/sourcesampledatatrackids-7i02t.md)
  The identifiers of source sample data tracks in the composition that the object requires to compose frames.
### Specifying a custom compositor
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](avmutablevideocomposition/customvideocompositorclass.md)
  The custom compositor class to use.

## Relationships

### Inherits From
- [AVVideoComposition](avvideocomposition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Editing and Playing HDR Video](editing-and-playing-hdr-video.md)
  Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md)
  Resolve common problems when creating compositions, video compositions, and audio mixes.
- [class AVVideoComposition](avvideocomposition.md)
  An object that describes how to compose video frames at particular points in time.
- [class AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)
  An operation that a compositor performs.
- [class AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.
- [class AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [class AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition)*