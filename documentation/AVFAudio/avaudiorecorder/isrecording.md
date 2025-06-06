# isRecording

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the audio recorder is recording.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var isRecording: Bool { get }
```

## See Also

- [func prepareToRecord() -> Bool](avaudiorecorder/preparetorecord.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](avaudiorecorder/record.md)
  Starts or resumes audio recording.
- [func record(atTime: TimeInterval) -> Bool](avaudiorecorder/record(attime:).md)
  Records audio starting at a specific time.
- [func record(forDuration: TimeInterval) -> Bool](avaudiorecorder/record(forduration:).md)
  Records audio for the indicated duration of time.
- [func record(atTime: TimeInterval, forDuration: TimeInterval) -> Bool](avaudiorecorder/record(attime:forduration:).md)
  Records audio starting at a specific time for the indicated duration.
- [func pause()](avaudiorecorder/pause.md)
  Pauses an audio recording.
- [func stop()](avaudiorecorder/stop.md)
  Stops recording and closes the audio file.
- [func deleteRecording() -> Bool](avaudiorecorder/deleterecording.md)
  Deletes a recorded audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/isrecording)*