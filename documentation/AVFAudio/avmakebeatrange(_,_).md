# AVMakeBeatRange(_:_:)

**Framework**: AVFAudio  
**Kind**: func  
**Role**: Function

Creates a beat range with the specified start time and length.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func AVMakeBeatRange(_ startBeat: AVMusicTimeStamp, _ lengthInBeats: AVMusicTimeStamp) -> AVBeatRange
```

```c
static AVBeatRange AVMakeBeatRange(AVMusicTimeStamp startBeat, AVMusicTimeStamp lengthInBeats);
```

## Parameters

- `startBeat`: The timestamp for the start position.
- `lengthInBeats`: The length of the beat range, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmakebeatrange(_:_:))*