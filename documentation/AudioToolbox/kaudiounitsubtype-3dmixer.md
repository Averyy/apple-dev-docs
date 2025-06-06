# kAudioUnitSubType_3DMixer

**Framework**: Audio Toolbox  
**Kind**: var

An audio unit that can have any number of input buses and one output bus. Each input bus can be mono, in which case it can be panned using 3D coordinates and parameters. Stereo input buses pass directly through to the output. Four-channel  inputs are rendered to the output configuration. The single output bus can be configured with 2, 4, 5, 6, 7 or 8 channels.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var kAudioUnitSubType_3DMixer: UInt32 { get }
```

## See Also

- [var kAudioUnitSubType_StereoMixer: UInt32](kaudiounitsubtype_stereomixer.md)
  An audio unit that can have any number of input buses, each of which is mono or stereo, and one stereo output bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_3dmixer)*