# record(atTime:forDuration:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) recordAtTime:(NSTimeInterval) time forDuration:(NSTimeInterval) duration;
```

## Return Value

[`true`](../../Swift/true.md) if recording was successful; otherwise, [`false`](../../Swift/false.md).

## Discussion

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

Calling this method implicitly calls [`prepareToRecord()`](./preparetorecord%28%29.md), which creates an audio file and prepares the system for recording.

## Parameters

- `time`: The time at which to start recording, relative to [`deviceCurrentTime`](./devicecurrenttime.md).
- `duration`: The duration of time to record, in seconds.

## See Also

### Controlling recording
- [func prepareToRecord() -> Bool](./preparetorecord%28%29.md)
  Creates an audio file and prepares the system for recording.
- [func record() -> Bool](./record%28%29.md)
  Starts or resumes audio recording.
- [func record(atTime: TimeInterval) -> Bool](./record%28attime%29.md)
  Records audio starting at a specific time.
- [func record(forDuration: TimeInterval) -> Bool](./record%28forduration%29.md)
  Records audio for the indicated duration of time.
- [func pause()](./pause%28%29.md)
  Pauses an audio recording.
- [func stop()](./stop%28%29.md)
  Stops recording and closes the audio file.
- [var isRecording: Bool](./isrecording.md)
  A Boolean value that indicates whether the audio recorder is recording.
- [func deleteRecording() -> Bool](./deleterecording%28%29.md)
  Deletes a recorded audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/record(attime:forduration:))*