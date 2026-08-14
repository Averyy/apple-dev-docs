# record(forDuration:)

**Framework**: AVFAudio  
**Kind**: method

Records audio for the indicated duration of time.

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
func record(forDuration duration: TimeInterval) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The recorder stops recording when it reaches the indicated duration.

Calling this method implicitly calls [`prepareToRecord()`](avaudiorecorder/preparetorecord().md), which creates an audio file and prepares the system for recording.

## Parameters

- `duration`: The duration of time to record, in seconds.

## See Also

- [func prepareToRecord() -> Bool](avaudiorecorder/preparetorecord.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](avaudiorecorder/record.md)
  Starts or resumes audio recording.
- [func record(atTime: TimeInterval) -> Bool](avaudiorecorder/record(attime:).md)
  Records audio starting at a specific time.
- [func record(atTime: TimeInterval, forDuration: TimeInterval) -> Bool](avaudiorecorder/record(attime:forduration:).md)
  Records audio starting at a specific time for the indicated duration.
- [func pause()](avaudiorecorder/pause.md)
  Pauses an audio recording.
- [func stop()](avaudiorecorder/stop.md)
  Stops recording and closes the audio file.
- [var isRecording: Bool](avaudiorecorder/isrecording.md)
  A Boolean value that indicates whether the audio recorder is recording.
- [func deleteRecording() -> Bool](avaudiorecorder/deleterecording.md)
  Deletes a recorded audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/record(forduration:))*