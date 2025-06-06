# audioOutputDeviceUniqueID

**Framework**: AVFoundation  
**Kind**: property

Specifies the unique ID of the Core Audio output device used to play audio.

**Availability**:
- macOS 10.9+

## Declaration

```swift
nonisolated
var audioOutputDeviceUniqueID: String? { get set }
```

#### Discussion

The default value of this property is `nil`, indicating that the default audio output device is used. Otherwise the value of this property is a string containing the unique ID of the Core Audio output device to be used for audio output.

Core Audio’s [`kAudioDevicePropertyDeviceUID`](https://developer.apple.com/documentation/CoreAudio/kAudioDevicePropertyDeviceUID) is a suitable source of audio output device unique IDs.

## See Also

- [var preferredVideoDecoderGPURegistryID: UInt64](avplayer/preferredvideodecodergpuregistryid.md)
  The registry identifier for the GPU used for video decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/audiooutputdeviceuniqueid)*