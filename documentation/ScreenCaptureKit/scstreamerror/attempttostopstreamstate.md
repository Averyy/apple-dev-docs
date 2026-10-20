# attemptToStopStreamState

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Type Property

An error message that indicates a stream is already stopped or doesn’t exist when trying to stop a stream.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var attemptToStopStreamState: SCStreamError.Code { get }
```

## See Also

### Stream management
- [static var attemptToStartStreamState: SCStreamError.Code](./attempttostartstreamstate.md)
  An error message that indicates a stream is already running or doesn’t exist when trying to start a stream.
- [static var attemptToUpdateFilterState: SCStreamError.Code](./attempttoupdatefilterstate.md)
  An error message that indicates a stream couldn’t update its content filter.
- [static var attemptToConfigState: SCStreamError.Code](./attempttoconfigstate.md)
  An error message that indicates a stream couldn’t update its configuration.
- [static var failedToStart: SCStreamError.Code](./failedtostart.md)
  An error message that indicates a stream failed to start.
- [static var failedToStartAudioCapture: SCStreamError.Code](./failedtostartaudiocapture.md)
  An error message that indicates an audio stream failed to start.
- [static var failedToStopAudioCapture: SCStreamError.Code](./failedtostopaudiocapture.md)
  An error message that indicates an audio stream failed to stop.
- [static var failedToStartMicrophoneCapture: SCStreamError.Code](./failedtostartmicrophonecapture.md)
  An error message that indicates microphone capture failed to start.
- [static var systemStoppedStream: SCStreamError.Code](./systemstoppedstream.md)
  An error message that indicates the system stopped the stream.
- [static var internalError: SCStreamError.Code](./internalerror.md)
  An error message that indicates a stream can’t start due to a failure in ScreenCaptureKit’s internals.
- [static var removingStream: SCStreamError.Code](./removingstream.md)
  An error message that indicates a stream wasn’t removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/attempttostopstreamstate)*