# kMTAudioProcessingTapFlag_EndOfStream

**Framework**: Media Toolbox  
**Kind**: var

Signifies that the source audio is past the end of stream.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var kMTAudioProcessingTapFlag_EndOfStream: MTAudioProcessingTapFlags { get }
```

#### Discussion

This happens when the audio queue is being stopped asynchronously and has finished playing all of its data. Returned from GetSourceAudio and should be propagated on return from the process callback.

## See Also

- [var kMTAudioProcessingTapFlag_StartOfStream: MTAudioProcessingTapFlags](kmtaudioprocessingtapflag_startofstream.md)
  Signifies that the source audio is the beginning of a continuous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/kmtaudioprocessingtapflag_endofstream)*