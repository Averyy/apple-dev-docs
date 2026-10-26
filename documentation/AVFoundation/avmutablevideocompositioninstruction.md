# AVMutableVideoCompositionInstruction

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A mutable video composition instruction subclass.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use [`AVVideoCompositionInstruction.Configuration`](./avvideocompositioninstruction-swift.class/configuration.md) instead.

## Declaration

```swift
class AVMutableVideoCompositionInstruction
```

```objc
@interface AVMutableVideoCompositionInstruction : AVVideoCompositionInstruction
```

#### Overview

An [`AVVideoComposition`](./avvideocomposition.md) object maintains an array of [`instructions`](./avvideocomposition/instructions.md) to perform its composition.

## Topics

### Configuring the instructions
- [var backgroundColor: CGColor?](./avmutablevideocompositioninstruction/backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](./avmutablevideocompositioninstruction/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](./avmutablevideocompositioninstruction/timerange.md)
  The time range to which the instruction applies.
- [var enablePostProcessing: Bool](./avmutablevideocompositioninstruction/enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.
### Configuring source tracks
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](./avmutablevideocompositioninstruction/requiredsourcesampledatatrackids.md)
  The track identifiers of source sample data that the compositor requires to compose frames for the instruction.
### Creating an instruction
- [+ videoCompositionInstruction](./avmutablevideocompositioninstruction/videocompositioninstruction.md)
  Returns a new mutable video composition instruction.

## Relationships

### Inherits From
- [AVVideoCompositionInstruction](./avvideocompositioninstruction-swift.class.md)
### Conforms To
- [AVVideoCompositionInstructionProtocol](./avvideocompositioninstructionprotocol.md)
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
- [class AVMutableVideoCompositionLayerInstruction](./avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction)*