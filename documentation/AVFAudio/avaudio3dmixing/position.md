# position

**Framework**: AVFAudio  
**Kind**: property  
**Required**: Yes

The location of the source in the 3D environment.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var position: AVAudio3DPoint { get set }
```

#### Discussion

The system specifies the coordinates in meters. Only the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) class implements this property.

## See Also

- [var obstruction: Float](avaudio3dmixing/obstruction.md)
  A value that simulates filtering of the direct path of sound due to an obstacle.
- [var occlusion: Float](avaudio3dmixing/occlusion.md)
  A value that simulates filtering of the direct and reverb paths of sound due to an obstacle.
- [var rate: Float](avaudio3dmixing/rate.md)
  A value that changes the playback rate of the input signal.
- [var pointSourceInHeadMode: AVAudio3DMixingPointSourceInHeadMode](avaudio3dmixing/pointsourceinheadmode.md)
  The in-head mode for a point source.
- [var reverbBlend: Float](avaudio3dmixing/reverbblend.md)
  A value that controls the blend of dry and reverb processed audio.
- [var sourceMode: AVAudio3DMixingSourceMode](avaudio3dmixing/sourcemode.md)
  The source mode for the input bus of the audio environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixing/position)*