# AVVideoComposition

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that describes how to compose video frames at particular points in time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVVideoComposition
```

```objc
@interface AVVideoComposition : NSObject
```

#### Overview

If you use the built-in video compositor, the instructions a video composition contain can specify a spatial transformation, an opacity value, and a cropping rectangle for each video source. This values can vary over time by applying linear ramping functions.

You can create a custom video compositor by implementing the [`AVVideoCompositing`](./avvideocompositing.md) protocol. The system provides the custom video compositor with pixel buffers for each of its video sources during playback, and can perform arbitrary graphical operations on them to produce visual output.

## Topics

### Creating a video composition
- [convenience init(configuration: AVVideoComposition.Configuration)](./avvideocomposition/init%28configuration%29.md)
  Initialize an AVVideoComposition with a configuration.
- [AVVideoComposition.Configuration](./avvideocomposition/configuration.md)
  Configurable properties for initializing a new AVVideoComposition instance.
- [convenience init(applyingFiltersTo: AVAsset, applier: (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws](./avvideocomposition/init%28applyingfiltersto,applier%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./avvideocomposition/videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](./avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [struct AVCIImageFilteringParameters](./avciimagefilteringparameters.md)
- [struct AVCIImageFilteringResult](./avciimagefilteringresult.md)
  An output video frame processed with Core Image filtering.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./avvideocomposition/videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](./avvideocomposition/init%28propertiesof%29.md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./avvideocomposition/init%28asset,applyingcifilterswithhandler%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithVideoComposition:](./avvideocomposition/videocompositionwithvideocomposition_.md)
  Pass-through initializer, for internal use in AVFoundation only
### Inspecting the video composition
- [var renderSize: CGSize](./avvideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./avvideocomposition/renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](./avvideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./avvideocomposition/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [var colorPrimaries: String?](./avvideocomposition/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](./avvideocomposition/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](./avvideocomposition/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](./avvideocomposition/customvideocompositorclass.md)
  A custom compositor class to use.
- [var outputBufferDescription: [[CMTag]]?](./avvideocomposition/outputbufferdescription-3ayt8.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](./avvideocomposition/spatialvideoconfigurations-80iab.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [struct AVSpatialVideoConfiguration](./avspatialvideoconfiguration-swift.struct.md)
- [outputBufferDescription](./avvideocomposition/outputbufferdescription-3wsar.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.
- [spatialVideoConfigurations](./avvideocomposition/spatialvideoconfigurations-2ipps.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [AVSpatialVideoConfiguration](./avspatialvideoconfiguration-c.class.md)
  An AVSpatialVideoConfiguration specifies spatial video properties.
### Validating the time range
- [func isValid(for: [AVAssetTrack], assetDuration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](./avvideocomposition/isvalid%28for,assetduration,timerange,validationdelegate%29.md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [protocol AVVideoCompositionValidationHandling](./avvideocompositionvalidationhandling.md)
  Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [func determineValidity(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: (Bool, (any Error)?) -> Void)](./avvideocomposition/determinevalidity%28for,timerange,validationdelegate,completionhandler%29.md)
  Determines whether the time ranges of the composition’s instructions conform to validation requirements.
- [func isValid(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool](./avvideocomposition/isvalid%28for,timerange,validationdelegate%29.md)
  Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
### Reading instructions
- [var instructions: [any AVVideoCompositionInstructionProtocol]](./avvideocomposition/instructions.md)
  The video composition instructions.
- [protocol AVVideoCompositionInstructionProtocol](./avvideocompositioninstructionprotocol.md)
  A protocol that defines the interface for a video composition instruction.
### Identifying source tracks
- [var sourceTrackIDForFrameTiming: CMPersistentTrackID](./avvideocomposition/sourcetrackidforframetiming.md)
  An identifier of the source track from which the video composition derives frame timing.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](./avvideocomposition/sourcesampledatatrackids-2hgue.md)
  The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [sourceSampleDataTrackIDs](./avvideocomposition/sourcesampledatatrackids-3nrgi.md)
  The identifiers of source sample data tracks in the composition that the compositor requires to compose frames.
### Configuring HDR metadata
- [var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](./avvideocomposition/perframehdrdisplaymetadatapolicy-swift.property.md)
  The policy for display of HDR display metadata on the rendered frame.
- [AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](./avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct.md)
  A type that defines the policy for handling of per frame HDR metadata.
### Initializers
- [init(propertiesOfAsset: AVAsset)](./avvideocomposition/init%28propertiesofasset%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVMutableVideoComposition](./avmutablevideocomposition.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Built-in video compositing
- [Editing and playing HDR video](./editing-and-playing-hdr-video.md)
  Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](./debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md)
  Resolve common problems when creating compositions, video compositions, and audio mixes.
- [class AVVideoCompositionInstruction](./avvideocompositioninstruction-swift.class.md)
  An operation that a compositor performs.
- [class AVVideoCompositionLayerInstruction](./avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [class AVMutableVideoComposition](./avmutablevideocomposition.md)
  A mutable video composition subclass.
- [class AVMutableVideoCompositionInstruction](./avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.
- [class AVMutableVideoCompositionLayerInstruction](./avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition)*