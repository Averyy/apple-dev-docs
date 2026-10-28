# AVAudio3DMixingPointSourceInHeadMode

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The in-head modes for a point source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAudio3DMixingPointSourceInHeadMode
```

```c
enum AVAudio3DMixingPointSourceInHeadMode : NSInteger;
```

## Overview

The in-head mode that determines what happens when a [`AVAudio3DMixingSourceMode.pointSource`](./avaudio3dmixingsourcemode/pointsource.md) moves inside the head of the listener. The in-head mode applies when using the [`AVAudio3DMixingRenderingAlgorithm.auto`](./avaudio3dmixingrenderingalgorithm/auto.md) rendering algorithm.

## Topics

### Creating an in-head mode
- [init?(rawValue: Int)](./avaudio3dmixingpointsourceinheadmode/init%28rawvalue%29.md)
### Choosing an in-head mode
- [AVAudio3DMixingPointSourceInHeadMode.mono](./avaudio3dmixingpointsourceinheadmode/mono.md)
  The point source remains a single mono source inside the head of the listener regardless of the channels it consists of.
- [AVAudio3DMixingPointSourceInHeadMode.bypass](./avaudio3dmixingpointsourceinheadmode/bypass.md)
  The point source distributes into each output channel inside the head of the listener.

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
- [var reverbBlend: Float](./avaudio3dmixing/reverbblend.md)
  A value that controls the blend of dry and reverb processed audio.
- [var sourceMode: AVAudio3DMixingSourceMode](./avaudio3dmixing/sourcemode.md)
  The source mode for the input bus of the audio environment node.
- [enum AVAudio3DMixingSourceMode](./avaudio3dmixingsourcemode.md)
  The source modes for the input bus of the audio environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingpointsourceinheadmode)*