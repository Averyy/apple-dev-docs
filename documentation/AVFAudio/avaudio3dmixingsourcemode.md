# AVAudio3DMixingSourceMode

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The source modes for the input bus of the audio environment node.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAudio3DMixingSourceMode
```

```c
enum AVAudio3DMixingSourceMode : NSInteger;
```

#### Overview

The source mode determines how the individual channels of an input bus distribute in space.

## Topics

### Creating a source mode
- [init?(rawValue: Int)](./avaudio3dmixingsourcemode/init%28rawvalue%29.md)
### Choosing a source mode
- [AVAudio3DMixingSourceMode.spatializeIfMono](./avaudio3dmixingsourcemode/spatializeifmono.md)
  A mono input bus that renders as a point source at the location of the source node.
- [AVAudio3DMixingSourceMode.bypass](./avaudio3dmixingsourcemode/bypass.md)
  A mode that does no spatial rendering.
- [AVAudio3DMixingSourceMode.pointSource](./avaudio3dmixingsourcemode/pointsource.md)
  All channels of the bus render as a single source at the location of the source node.
- [AVAudio3DMixingSourceMode.ambienceBed](./avaudio3dmixingsourcemode/ambiencebed.md)
  The input channels spread around the listener as far-field sources that anchor to global space.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the 3D mixing parameters
- [var obstruction: Float](./avaudio3dmixing/obstruction.md)
  A value that simulates filtering of the direct path of sound due to an obstacle.
- [var occlusion: Float](./avaudio3dmixing/occlusion.md)
  A value that simulates filtering of the direct and reverb paths of sound due to an obstacle.
- [var position: AVAudio3DPoint](./avaudio3dmixing/position.md)
  The location of the source in the 3D environment.
- [var rate: Float](./avaudio3dmixing/rate.md)
  A value that changes the playback rate of the input signal.
- [var pointSourceInHeadMode: AVAudio3DMixingPointSourceInHeadMode](./avaudio3dmixing/pointsourceinheadmode.md)
  The in-head mode for a point source.
- [enum AVAudio3DMixingPointSourceInHeadMode](./avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [var reverbBlend: Float](./avaudio3dmixing/reverbblend.md)
  A value that controls the blend of dry and reverb processed audio.
- [var sourceMode: AVAudio3DMixingSourceMode](./avaudio3dmixing/sourcemode.md)
  The source mode for the input bus of the audio environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingsourcemode)*