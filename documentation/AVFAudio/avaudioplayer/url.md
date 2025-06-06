# url

**Framework**: AVFAudio  
**Kind**: property

The URL of the audio file.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

This property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if you don’t create the player with a URL.

## See Also

- [var data: Data?](avaudioplayer/data.md)
  The audio data associated with the player.
- [var format: AVAudioFormat](avaudioplayer/format.md)
  The format of the player’s audio data.
- [var settings: [String : Any]](avaudioplayer/settings.md)
  A dictionary that provides information about the player’s audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/url)*