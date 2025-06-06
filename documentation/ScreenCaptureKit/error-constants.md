# Error Constants

**Framework**: ScreenCaptureKit

Error code constants for framework operations.

## Topics

### User cancellation
- [static var userStopped: SCStreamError.Code](scstreamerror/userstopped.md)
  An error message that indicates the user stopped the stream.
### Privacy and entitlements
- [static var userDeclined: SCStreamError.Code](scstreamerror/userdeclined.md)
  An error message that indicates the user didn’t grant Screen Recording permission to your app.
- [static var missingEntitlements: SCStreamError.Code](scstreamerror/missingentitlements.md)
  An error message that indicates missing entitlements in your app.
### Stream management
- [static var attemptToStartStreamState: SCStreamError.Code](scstreamerror/attempttostartstreamstate.md)
  An error message that indicates a stream is already running or doesn’t exist when trying to start a stream.
- [static var attemptToStopStreamState: SCStreamError.Code](scstreamerror/attempttostopstreamstate.md)
  An error message that indicates a stream is already stopped or doesn’t exist when trying to stop a stream.
- [static var attemptToUpdateFilterState: SCStreamError.Code](scstreamerror/attempttoupdatefilterstate.md)
  An error message that indicates a stream couldn’t update its content filter.
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
### Shareable content
- [static var noCaptureSource: SCStreamError.Code](scstreamerror/nocapturesource.md)
  An error message that indicates a stream doesn’t have a source to capture.
- [static var noDisplayList: SCStreamError.Code](scstreamerror/nodisplaylist.md)
  An error message that indicates a stream doesn’t have displays available.
- [static var noWindowList: SCStreamError.Code](scstreamerror/nowindowlist.md)
  An error message that indicates a stream doesn’t have windows available.
- [static var failedApplicationConnectionInvalid: SCStreamError.Code](scstreamerror/failedapplicationconnectioninvalid.md)
  An error message that indicates the stream lost its connection to an app.
- [static var failedApplicationConnectionInterrupted: SCStreamError.Code](scstreamerror/failedapplicationconnectioninterrupted.md)
  An error message that indicates there was an interruption in a connection to an app.
- [static var failedNoMatchingApplicationContext: SCStreamError.Code](scstreamerror/failednomatchingapplicationcontext.md)
  An error message that indicates there isn’t a matching app context for streaming.
### Invalid parameters
- [static var invalidParameter: SCStreamError.Code](scstreamerror/invalidparameter.md)
  An error message that indicates an operation failed because of an invalid parameter value.

## See Also

- [SCStreamError.Code](scstreamerror/code.md)
  Codes for user cancellation events and errors that can occur in ScreenCaptureKit.
- [static var errorDomain: String](scstreamerror/errordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/error-constants)*