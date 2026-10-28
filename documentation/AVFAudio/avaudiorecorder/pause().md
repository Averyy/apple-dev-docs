# pause()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Pauses an audio recording.

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
func pause()
```

```objc
- (void) pause;
```

## Discussion

Call [`record()`](./record%28%29.md) to resume recording.

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
- [func record(atTime: TimeInterval, forDuration: TimeInterval) -> Bool](./record%28attime,forduration%29.md)
  Records audio starting at a specific time for the indicated duration.
- [func stop()](./stop%28%29.md)
  Stops recording and closes the audio file.
- [var isRecording: Bool](./isrecording.md)
  A Boolean value that indicates whether the audio recorder is recording.
- [func deleteRecording() -> Bool](./deleterecording%28%29.md)
  Deletes a recorded audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/pause())*