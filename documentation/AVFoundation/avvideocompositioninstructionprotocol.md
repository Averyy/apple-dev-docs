# AVVideoCompositionInstructionProtocol

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the interface for a video composition instruction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVVideoCompositionInstructionProtocol : NSObjectProtocol
```

#### Overview

A video composition maintains an array of instructions that describe how to compose its content.

## Topics

### Getting Track ID Settings
- [var passthroughTrackID: CMPersistentTrackID](avvideocompositioninstructionprotocol/passthroughtrackid.md)
  An identifier of a source track to pass through without compositing.
- [var requiredSourceTrackIDs: [NSValue]?](avvideocompositioninstructionprotocol/requiredsourcetrackids.md)
  The identifiers of the video tracks the instruction requires to compose frames.
- [var requiredSourceSampleDataTrackIDs: [NSNumber]](avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids.md)
  The identifiers of the sample data tracks the instruction requires to compose frames.
### Getting Tweening Settings
- [var containsTweening: Bool](avvideocompositioninstructionprotocol/containstweening.md)
  A Boolean value that indicates whether the composition contains tweening.
### Getting Post-Processing Status
- [var enablePostProcessing: Bool](avvideocompositioninstructionprotocol/enablepostprocessing.md)
  A Boolean value that indicates whether the composition enables post-processing.
### Getting Timing Settings
- [var timeRange: CMTimeRange](avvideocompositioninstructionprotocol/timerange.md)
  The time range during which the instruction is effective.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)

## See Also

- [var instructions: [any AVVideoCompositionInstructionProtocol]](avmutablevideocomposition/instructions.md)
  The video composition instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol)*