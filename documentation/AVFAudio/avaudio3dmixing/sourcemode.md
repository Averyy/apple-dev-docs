# sourceMode

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The source mode for the input bus of the audio environment node.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var sourceMode: AVAudio3DMixingSourceMode { get set }
```

```objc
@property (nonatomic) AVAudio3DMixingSourceMode sourceMode;
```

## See Also

### Getting the 3D mixing parameters
- [var obstruction: Float](./obstruction.md)
  A value that simulates filtering of the direct path of sound due to an obstacle.
- [var occlusion: Float](./occlusion.md)
  A value that simulates filtering of the direct and reverb paths of sound due to an obstacle.
- [var position: AVAudio3DPoint](./position.md)
  The location of the source in the 3D environment.
- [var rate: Float](./rate.md)
  A value that changes the playback rate of the input signal.
- [var pointSourceInHeadMode: AVAudio3DMixingPointSourceInHeadMode](./pointsourceinheadmode.md)
  The in-head mode for a point source.
- [enum AVAudio3DMixingPointSourceInHeadMode](../avaudio3dmixingpointsourceinheadmode.md)
  The in-head modes for a point source.
- [var reverbBlend: Float](./reverbblend.md)
  A value that controls the blend of dry and reverb processed audio.
- [enum AVAudio3DMixingSourceMode](../avaudio3dmixingsourcemode.md)
  The source modes for the input bus of the audio environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixing/sourcemode)*