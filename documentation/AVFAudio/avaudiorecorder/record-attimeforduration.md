# record(atTime:forDuration:)

**Framework**: AVFAudio  
**Kind**: method

Records audio starting at a specific time for the indicated duration.

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
func record(atTime time: TimeInterval, forDuration duration: TimeInterval) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if recording was successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The recorder automatically stops recording when it reaches the indicated duration. You may also use it to synchronize recording of multiple recorders as shown below.

```swift
func startSynchronizedRecording() {
    // Create a start time relative to the current device time.
    let time = recorderOne.deviceCurrentTime + 0.01
    let duration: TimeInterval = 10.0
    
    // Synchronize recording of both recorders.
    recorderOne.record(atTime: time, forDuration: duration)
    recorderTwo.record(atTime: time, forDuration: duration)
}
```

Calling this method implicitly calls [`prepareToRecord()`](avaudiorecorder/preparetorecord().md), which creates an audio file and prepares the system for recording.

## Parameters

- `time`: The time at which to start recording, relative to  .
- `duration`: The duration of time to record, in seconds.

## See Also

- [func prepareToRecord() -> Bool](avaudiorecorder/preparetorecord.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](avaudiorecorder/record.md)
  Starts or resumes audio recording.
- [func record(atTime: TimeInterval) -> Bool](avaudiorecorder/record(attime:).md)
  Records audio starting at a specific time.
- [func record(forDuration: TimeInterval) -> Bool](avaudiorecorder/record(forduration:).md)
  Records audio for the indicated duration of time.
- [func pause()](avaudiorecorder/pause.md)
  Pauses an audio recording.
- [func stop()](avaudiorecorder/stop.md)
  Stops recording and closes the audio file.
- [var isRecording: Bool](avaudiorecorder/isrecording.md)
  A Boolean value that indicates whether the audio recorder is recording.
- [func deleteRecording() -> Bool](avaudiorecorder/deleterecording.md)
  Deletes a recorded audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/record(attime:forduration:))*