# attemptToUpdateFilterState

**Framework**: ScreenCaptureKit  
**Kind**: property

An error message that indicates a stream couldn’t update its content filter.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static var attemptToUpdateFilterState: SCStreamError.Code { get }
```

## See Also

- [static var attemptToStartStreamState: SCStreamError.Code](scstreamerror/attempttostartstreamstate.md)
  An error message that indicates a stream is already running or doesn’t exist when trying to start a stream.
- [static var attemptToStopStreamState: SCStreamError.Code](scstreamerror/attempttostopstreamstate.md)
  An error message that indicates a stream is already stopped or doesn’t exist when trying to stop a stream.
- [static var attemptToConfigState: SCStreamError.Code](scstreamerror/attempttoconfigstate.md)
  An error message that indicates a stream couldn’t update its configuration.
- [static var failedToStart: SCStreamError.Code](scstreamerror/failedtostart.md)
  An error message that indicates a stream failed to start.
- [static var failedToStartAudioCapture: SCStreamError.Code](scstreamerror/failedtostartaudiocapture.md)
  An error message that indicates an audio stream failed to start.
- [static var failedToStopAudioCapture: SCStreamError.Code](scstreamerror/failedtostopaudiocapture.md)
  An error message that indicates an audio stream failed to stop.
- [static var failedToStartMicrophoneCapture: SCStreamError.Code](scstreamerror/failedtostartmicrophonecapture.md)
  An error message that indicates microphone capture failed to start.
- [static var systemStoppedStream: SCStreamError.Code](scstreamerror/systemstoppedstream.md)
  An error message that indicates the system stopped the stream.
- [static var internalError: SCStreamError.Code](scstreamerror/internalerror.md)
  An error message that indicates a stream can’t start due to a failure in ScreenCaptureKit’s internals.
- [static var removingStream: SCStreamError.Code](scstreamerror/removingstream.md)
  An error message that indicates a stream wasn’t removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/attempttoupdatefilterstate)*