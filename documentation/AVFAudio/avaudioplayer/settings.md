# settings

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A dictionary that provides information about the player’s audio data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var settings: [String : Any] { get }
```

```objc
@property (readonly) NSDictionary<NSString *,id> * settings;
```

## See Also

### Inspecting the audio data
- [var url: URL?](./url.md)
  The URL of the audio file.
- [var data: Data?](./data.md)
  The audio data associated with the player.
- [var format: AVAudioFormat](./format.md)
  The format of the player’s audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/settings)*