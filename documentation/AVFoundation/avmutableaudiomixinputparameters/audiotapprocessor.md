# audioTapProcessor

**Framework**: AVFoundation  
**Kind**: property

The audio processing tap associated with the track.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioTapProcessor: MTAudioProcessingTap? { get set }
```

#### Discussion

You can use this property to associate an audio tap with the audio track. You can use the audio tap to access the audio data before it is played, read, or exported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/audiotapprocessor)*