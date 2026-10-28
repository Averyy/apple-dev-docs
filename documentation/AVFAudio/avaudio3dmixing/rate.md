# rate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A value that changes the playback rate of the input signal.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var rate: Float { get set }
```

```objc
@property (nonatomic) float rate;
```

## Discussion

A value of `2.0` results in the output audio playing one octave higher. A value of `0.5` results in the output audio playing one octave lower.

The default value is `1.0`, and the range of valid values is `0.5` to `2.0`. Only the [`AVAudioEnvironmentNode`](../avaudioenvironmentnode.md) class implements this property.

## See Also

### Getting the 3D mixing parameters
- [var obstruction: Float](./obstruction.md)
  A value that simulates filtering of the direct path of sound due to an obstacle.
- [var occlusion: Float](./occlusion.md)
  A value that simulates filtering of the direct and reverb paths of sound due to an obstacle.
- [var position: AVAudio3DPoint](./position.md)
  The location of the source in the 3D environment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixing/rate)*