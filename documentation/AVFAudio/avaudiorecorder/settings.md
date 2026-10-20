# settings

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The settings that describe the format of the recorded audio.

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
var settings: [String : Any] { get }
```

```objc
@property (readonly) NSDictionary<NSString *,id> * settings;
```

#### Discussion

See [`init(url:settings:)`](./init%28url,settings%29-5whyq.md) for supported keys and values.

## See Also

### Inspecting the audio data
- [var url: URL](./url.md)
  The URL to which the recorder writes its data.
- [var format: AVAudioFormat](./format.md)
  The format of the recorded audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/settings)*