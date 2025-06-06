# kAudioUnitSubType_StereoMixer

**Framework**: Audio Toolbox  
**Kind**: var

An audio unit that can have any number of input buses, each of which is mono or stereo, and one stereo output bus.

**Availability**:
- macOS ?+

## Declaration

```swift
var kAudioUnitSubType_StereoMixer: UInt32 { get }
```

## See Also

- [var kAudioUnitSubType_3DMixer: UInt32](kaudiounitsubtype_3dmixer.md)
  An audio unit that can have any number of input buses and one output bus. Each input bus can be mono, in which case it can be panned using 3D coordinates and parameters. Stereo input buses pass directly through to the output. Four-channel  inputs are rendered to the output configuration. The single output bus can be configured with 2, 4, 5, 6, 7 or 8 channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_stereomixer)*