# obstruction

**Framework**: AVFAudio  
**Kind**: property  
**Required**: Yes

A value that simulates filtering of the direct path of sound due to an obstacle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var obstruction: Float { get set }
```

#### Discussion

The value of `obstruction` is in decibels. The system blocks only the direct path of sound between the source and listener.

The default value is `0.0`, and the range of valid values is `-100` to `0`. Only the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) class implements this property.

## See Also

- [var occlusion: Float](avaudio3dmixing/occlusion.md)
  A value that simulates filtering of the direct and reverb paths of sound due to an obstacle.
- [var position: AVAudio3DPoint](avaudio3dmixing/position.md)
  The location of the source in the 3D environment.
- [var rate: Float](avaudio3dmixing/rate.md)
  A value that changes the playback rate of the input signal.
- [var pointSourceInHeadMode: AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixing/pointsourceinheadmode.md)
  The in-head mode for a point source.
- [var reverbBlend: Float](avaudio3dmixing/reverbblend.md)
  A value that controls the blend of dry and reverb processed audio.
- [var sourceMode: AVAudio3DMixingSourceMode](avaudio3dmixing/sourcemode.md)
  The source mode for the input bus of the audio environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixing/obstruction)*