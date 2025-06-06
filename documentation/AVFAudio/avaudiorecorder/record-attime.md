# record(atTime:)

**Framework**: AVFAudio  
**Kind**: method

Records audio starting at a specific time.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func record(atTime time: TimeInterval) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if recording starts successfully; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You can call this method on a single recorder, or use it to synchronize the recording of multiple players as shown below.

```swift
func startSynchronizedRecording() {
    // Create a time offset relative to the current device time.
    let timeOffset = recorderOne.deviceCurrentTime + 0.01
    
    // Synchronize the recording time of both recorders.
    recorderOne.record(atTime: timeOffset)
    recorderTwo.record(atTime: timeOffset)
}
```

Calling this method implicitly calls [`prepareToRecord()`](avaudiorecorder/preparetorecord().md), which creates an audio file and prepares the system for recording.

## Parameters

- `time`: The time at which to start recording, relative to  .

## See Also

- [func prepareToRecord() -> Bool](avaudiorecorder/preparetorecord.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](avaudiorecorder/record.md)
  Starts or resumes audio recording.
- [func record(forDuration: TimeInterval) -> Bool](avaudiorecorder/record(forduration:).md)
  Records audio for the indicated duration of time.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/record(attime:))*