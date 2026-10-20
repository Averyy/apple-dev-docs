# position

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The location of the source in the 3D environment.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var position: AVAudio3DPoint { get set }
```

```objc
@property (nonatomic) AVAudio3DPoint position;
```

#### Discussion

The system specifies the coordinates in meters. Only the [`AVAudioEnvironmentNode`](../avaudioenvironmentnode.md) class implements this property.

## See Also

### Getting the 3D mixing parameters
- [var obstruction: Float](./obstruction.md)
  A value that simulates filtering of the direct path of sound due to an obstacle.
- [var occlusion: Float](./occlusion.md)
  A value that simulates filtering of the direct and reverb paths of sound due to an obstacle.
- [var rate: Float](./rate.md)
  A value that changes the playback rate of the input signal.
- [var pointSourceInHeadMode: AVAudio3DMixingPointSourceInHeadMode](./pointsourceinheadmode.md)
  The in-head mode for a point source.
- [enum AVAudio3DMixingPointSourceInHeadMode](../avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [var reverbBlend: Float](./reverbblend.md)
  A value that controls the blend of dry and reverb processed audio.
- [var sourceMode: AVAudio3DMixingSourceMode](./sourcemode.md)
  The source mode for the input bus of the audio environment node.
- [enum AVAudio3DMixingSourceMode](../avaudio3dmixingsourcemode.md)
  The source modes for the input bus of the audio environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixing/position)*