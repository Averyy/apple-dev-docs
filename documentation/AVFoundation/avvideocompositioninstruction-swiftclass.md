# AVVideoCompositionInstruction

**Framework**: AVFoundation  
**Kind**: class

An operation that a compositor performs.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVVideoCompositionInstruction
```

#### Overview

An [`AVVideoComposition`](avvideocomposition.md) object maintains an array of [`instructions`](avvideocomposition/instructions.md) to perform its composition.

## Topics

### Creating an instruction
- [convenience init(configuration: AVVideoCompositionInstruction.Configuration)](avvideocompositioninstruction-swift.class/init(configuration:).md)
  Initialize an AVVideoCompositionInstruction with a configuration.
- [AVVideoCompositionInstruction.Configuration](avvideocompositioninstruction-swift.class/configuration.md)
  Configurable properties for initializing a new AVVideoCompositionInstruction instance.
### Inspecting the instruction
- [var backgroundColor: CGColor?](avvideocompositioninstruction-swift.class/backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avvideocompositioninstruction-swift.class/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](avvideocompositioninstruction-swift.class/timerange.md)
  The time range to which the instruction applies.
- [var enablePostProcessing: Bool](avvideocompositioninstruction-swift.class/enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.
### Identifying source tracks
- [var requiredSourceTrackIDs: [NSValue]](avvideocompositioninstruction-swift.class/requiredsourcetrackids.md)
  The identifiers of source video tracks that the compositor requires to compose frames for the instruction.
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids.md)
  The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [var passthroughTrackID: CMPersistentTrackID](avvideocompositioninstruction-swift.class/passthroughtrackid.md)
  The track identifier from an instruction source frame.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
### Conforms To
- [AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md)
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
- [class AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [class AVMutableVideoComposition](avmutablevideocomposition.md)
  A mutable video composition subclass.
- [class AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.
- [class AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class)*