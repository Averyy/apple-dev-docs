# kMTAudioProcessingTapFlag_StartOfStream

**Framework**: Media Toolbox  
**Kind**: var  
**Role**: Global Variable

Signifies that the source audio is the beginning of a continuous stream.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var kMTAudioProcessingTapFlag_StartOfStream: MTAudioProcessingTapFlags { get }
```

```c
kMTAudioProcessingTapFlag_StartOfStream
```

#### Discussion

Returned from [`MTAudioProcessingTapGetSourceAudio(_:_:_:_:_:_:)`](./mtaudioprocessingtapgetsourceaudio%28_,_,_,_,_,_%29.md).

## See Also

### Flags
- [var kMTAudioProcessingTapFlag_EndOfStream: MTAudioProcessingTapFlags](./kmtaudioprocessingtapflag_endofstream.md)
  Signifies that the source audio is past the end of stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/kmtaudioprocessingtapflag_startofstream)*