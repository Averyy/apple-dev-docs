# audioPlayerDecodeErrorDidOccur(_:error:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when an audio player encounters a decoding error during playback.

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
optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error: (any Error)?)
```

```objc
- (void) audioPlayerDecodeErrorDidOccur:(AVAudioPlayer *) player error:(NSError *) error;
```

## Parameters

- `player`: The audio player that encounters the decoding error.
- `error`: The decoding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayerdelegate/audioplayerdecodeerrordidoccur(_:error:))*