# format

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The format of the player’s audio data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var format: AVAudioFormat { get }
```

```objc
@property (readonly) AVAudioFormat * format;
```

## See Also

### Inspecting the audio data
- [var url: URL?](./url.md)
  The URL of the audio file.
- [var data: Data?](./data.md)
  The audio data associated with the player.
- [var settings: [String : Any]](./settings.md)
  A dictionary that provides information about the player’s audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/format)*