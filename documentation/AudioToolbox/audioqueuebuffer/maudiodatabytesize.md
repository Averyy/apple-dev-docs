# mAudioDataByteSize

**Framework**: Audio Toolbox  
**Kind**: property

The number of bytes of valid audio data in the audio queue buffer’s `mAudioData` field, initially set to `0`. Your callback must set this value for a playback audio queue; for recording, the recording audio queue sets the value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var mAudioDataByteSize: UInt32
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer/maudiodatabytesize)*