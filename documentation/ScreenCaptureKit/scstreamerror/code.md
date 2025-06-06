# SCStreamError.Code

**Framework**: ScreenCaptureKit  
**Kind**: enum

Codes for user cancellation events and errors that can occur in ScreenCaptureKit.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
enum Code
```

## Topics

### User cancellation
- [SCStreamError.Code.userStopped](scstreamerror/code/userstopped.md)
  An error message that indicates the user stopped the stream.
### Privacy and entitlements
- [SCStreamError.Code.userDeclined](scstreamerror/code/userdeclined.md)
  An error message that indicates the user didn’t grant Screen Recording permission to your app.
- [SCStreamError.Code.missingEntitlements](scstreamerror/code/missingentitlements.md)
  An error message that indicates missing entitlements in your app.
### Stream management
- [SCStreamError.Code.attemptToStartStreamState](scstreamerror/code/attempttostartstreamstate.md)
  An error message that indicates a stream is already running or doesn’t exist when trying to start a stream.
- [SCStreamError.Code.attemptToStopStreamState](scstreamerror/code/attempttostopstreamstate.md)
  An error message that indicates a stream is already stopped or doesn’t exist when trying to stop a stream.
- [SCStreamError.Code.attemptToUpdateFilterState](scstreamerror/code/attempttoupdatefilterstate.md)
  An error message that indicates a stream couldn’t update its content filter.
- [SCStreamError.Code.attemptToConfigState](scstreamerror/code/attempttoconfigstate.md)
  An error message that indicates a stream couldn’t update its configuration.
- [SCStreamError.Code.failedToStart](scstreamerror/code/failedtostart.md)
  An error message that indicates a stream failed to start.
- [SCStreamError.Code.removingStream](scstreamerror/code/removingstream.md)
  An error message that indicates a stream wasn’t removed.
- [SCStreamError.Code.failedToStartAudioCapture](scstreamerror/code/failedtostartaudiocapture.md)
  An error message that indicates an audio stream failed to start.
- [SCStreamError.Code.failedToStopAudioCapture](scstreamerror/code/failedtostopaudiocapture.md)
  An error message that indicates an audio stream failed to stop.
- [SCStreamError.Code.failedToStartMicrophoneCapture](scstreamerror/code/failedtostartmicrophonecapture.md)
  An error message that indicates microphone capture failed to start.
- [SCStreamError.Code.systemStoppedStream](scstreamerror/code/systemstoppedstream.md)
  An error message that indicates the system stopped the stream.
- [SCStreamError.Code.internalError](scstreamerror/code/internalerror.md)
  An error message that indicates a stream can’t start due to a failure in ScreenCaptureKit’s internals.
### Shareable content
- [SCStreamError.Code.noCaptureSource](scstreamerror/code/nocapturesource.md)
  An error message that indicates a stream doesn’t have a source to capture.
- [SCStreamError.Code.noDisplayList](scstreamerror/code/nodisplaylist.md)
  An error message that indicates a stream doesn’t have displays available.
- [SCStreamError.Code.noWindowList](scstreamerror/code/nowindowlist.md)
  An error message that indicates a stream doesn’t have windows available.
- [SCStreamError.Code.failedApplicationConnectionInvalid](scstreamerror/code/failedapplicationconnectioninvalid.md)
  An error message that indicates the stream lost its connection to an app.
- [SCStreamError.Code.failedApplicationConnectionInterrupted](scstreamerror/code/failedapplicationconnectioninterrupted.md)
  An error message that indicates there was an interruption in a connection to an app.
- [SCStreamError.Code.failedNoMatchingApplicationContext](scstreamerror/code/failednomatchingapplicationcontext.md)
  An error message that indicates there isn’t a matching app context for streaming.
### Invalid parameters
- [SCStreamError.Code.invalidParameter](scstreamerror/code/invalidparameter.md)
  An error message that indicates an operation failed because of an invalid parameter value.
### Creating an error
- [init?(rawValue: Int)](scstreamerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/code)*