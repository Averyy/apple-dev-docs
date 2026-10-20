# url

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The URL to which the recorder writes its data.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var url: URL { get }
```

```objc
@property (readonly) NSURL * url;
```

## See Also

### Inspecting the audio data
- [var format: AVAudioFormat](./format.md)
  The format of the recorded audio.
- [var settings: [String : Any]](./settings.md)
  The settings that describe the format of the recorded audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/url)*