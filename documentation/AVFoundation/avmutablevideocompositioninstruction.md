# AVMutableVideoCompositionInstruction

**Framework**: AVFoundation  
**Kind**: class

A mutable video composition instruction subclass.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVMutableVideoCompositionInstruction
```

#### Overview

An [`AVVideoComposition`](avvideocomposition.md) object maintains an array of [`instructions`](avvideocomposition/instructions.md) to perform its composition.

## Topics

### Configuring the Instructions
- [var backgroundColor: CGColor?](avmutablevideocompositioninstruction/backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avmutablevideocompositioninstruction/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](avmutablevideocompositioninstruction/timerange.md)
  The time range to which the instruction applies.
- [var enablePostProcessing: Bool](avmutablevideocompositioninstruction/enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.
### Configuring Source Tracks
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](avmutablevideocompositioninstruction/requiredsourcesampledatatrackids.md)
  The track identifiers of source sample data that the compositor requires to compose frames for the instruction.

## Relationships

### Inherits From
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)
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
- [class AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [class AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction)*