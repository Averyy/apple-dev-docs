# AVBeatRange

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

A specific time range within a music track.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef struct _AVBeatRange { ... } AVBeatRange;
```

## Topics

### Creating a beat range
- [func AVMakeBeatRange(AVMusicTimeStamp, AVMusicTimeStamp) -> AVBeatRange](./avmakebeatrange%28_,_%29.md)
  Creates a beat range with the specified start time and length.
### Inspecting a range
- [length](./avbeatrange-c.struct/length.md)
- [start](./avbeatrange-c.struct/start.md)

## See Also

### Handling beat range
- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](./avaudiosequencer/beats%28forhosttime,error%29.md)
  Gets the beat the system plays at the specified host time.
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](./avaudiosequencer/beats%28forseconds%29.md)
  Gets the beat position (timestamp) for the specified time in the track.
- [var AVMusicTimeStampEndOfTrack: Double](./avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avbeatrange-c.struct)*