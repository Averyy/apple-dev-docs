# record(atTime:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) recordAtTime:(NSTimeInterval) time;
```

## Return Value

[`true`](../../Swift/true.md) if recording starts successfully; otherwise, [`false`](../../Swift/false.md).

## Discussion

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

Calling this method implicitly calls [`prepareToRecord()`](./preparetorecord%28%29.md), which creates an audio file and prepares the system for recording.

## Parameters

- `time`: The time at which to start recording, relative to [`deviceCurrentTime`](./devicecurrenttime.md).

## See Also

### Controlling recording
- [func prepareToRecord() -> Bool](./preparetorecord%28%29.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](./record%28%29.md)
  Starts or resumes audio recording.
- [func record(forDuration: TimeInterval) -> Bool](./record%28forduration%29.md)
  Records audio for the indicated duration of time.
- [func record(atTime: TimeInterval, forDuration: TimeInterval) -> Bool](./record%28attime,forduration%29.md)
  Records audio starting at a specific time for the indicated duration.
- [func pause()](./pause%28%29.md)
  Pauses an audio recording.
- [func stop()](./stop%28%29.md)
  Stops recording and closes the audio file.
- [var isRecording: Bool](./isrecording.md)
  A Boolean value that indicates whether the audio recorder is recording.
- [func deleteRecording() -> Bool](./deleterecording%28%29.md)
  Deletes a recorded audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/record(attime:))*