# audioPlayerDidFinishPlaying(_:successfully:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the audio finishes playing.

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
optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool)
```

```objc
- (void) audioPlayerDidFinishPlaying:(AVAudioPlayer *) player successfully:(BOOL) flag;
```

#### Discussion

The system doesn’t call this method on an audio interruption.

## Parameters

- `player`: The audio player that finishes playing.
- `flag`: A Boolean value that indicates whether the audio finishes playing successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerdidfinishplaying(_:successfully:))*