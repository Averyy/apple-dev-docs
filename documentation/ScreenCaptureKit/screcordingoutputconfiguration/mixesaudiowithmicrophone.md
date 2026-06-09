# mixesAudioWithMicrophone

**Framework**: ScreenCaptureKit  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var mixesAudioWithMicrophone: Bool { get set }
```

#### Discussion

If the stream being recorded captures both system audio and microphone audio, setting mixesAudioWithMicrophone to NO will keep two audio tracks for each audio stream in the recording output. Default value is YES, which will mix system and microphone audio, result one audio track in recording output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingoutputconfiguration/mixesaudiowithmicrophone)*