# SCStreamError.Code

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

Codes for user cancellation events and errors that can occur in ScreenCaptureKit.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Code
```

```c
enum SCStreamErrorCode : NSInteger;
```

## Topics

### User cancellation
- [SCStreamError.Code.userStopped](./code/userstopped.md)
  An error message that indicates the user stopped the stream.
### Privacy and entitlements
- [SCStreamError.Code.userDeclined](./code/userdeclined.md)
  An error message that indicates the user didn’t grant Screen Recording permission to your app.
- [SCStreamError.Code.missingEntitlements](./code/missingentitlements.md)
  An error message that indicates missing entitlements in your app.
### Stream management
- [SCStreamError.Code.attemptToStartStreamState](./code/attempttostartstreamstate.md)
  An error message that indicates a stream is already running or doesn’t exist when trying to start a stream.
- [SCStreamError.Code.attemptToStopStreamState](./code/attempttostopstreamstate.md)
  An error message that indicates a stream is already stopped or doesn’t exist when trying to stop a stream.
- [SCStreamError.Code.attemptToUpdateFilterState](./code/attempttoupdatefilterstate.md)
  An error message that indicates a stream couldn’t update its content filter.
- [SCStreamError.Code.attemptToConfigState](./code/attempttoconfigstate.md)
  An error message that indicates a stream couldn’t update its configuration.
- [SCStreamError.Code.failedToStart](./code/failedtostart.md)
  An error message that indicates a stream failed to start.
- [SCStreamError.Code.removingStream](./code/removingstream.md)
  An error message that indicates a stream wasn’t removed.
- [SCStreamError.Code.failedToStartAudioCapture](./code/failedtostartaudiocapture.md)
  An error message that indicates an audio stream failed to start.
- [SCStreamError.Code.failedToStopAudioCapture](./code/failedtostopaudiocapture.md)
  An error message that indicates an audio stream failed to stop.
- [SCStreamError.Code.failedToStartMicrophoneCapture](./code/failedtostartmicrophonecapture.md)
  An error message that indicates microphone capture failed to start.
- [SCStreamError.Code.systemStoppedStream](./code/systemstoppedstream.md)
  An error message that indicates the system stopped the stream.
- [SCStreamError.Code.internalError](./code/internalerror.md)
  An error message that indicates a stream can’t start due to a failure in ScreenCaptureKit’s internals.
### Shareable content
- [SCStreamError.Code.noCaptureSource](./code/nocapturesource.md)
  An error message that indicates a stream doesn’t have a source to capture.
- [SCStreamError.Code.noDisplayList](./code/nodisplaylist.md)
  An error message that indicates a stream doesn’t have displays available.
- [SCStreamError.Code.noWindowList](./code/nowindowlist.md)
  An error message that indicates a stream doesn’t have windows available.
- [SCStreamError.Code.failedApplicationConnectionInvalid](./code/failedapplicationconnectioninvalid.md)
  An error message that indicates the stream lost its connection to an app.
- [SCStreamError.Code.failedApplicationConnectionInterrupted](./code/failedapplicationconnectioninterrupted.md)
  An error message that indicates there was an interruption in a connection to an app.
- [SCStreamError.Code.failedNoMatchingApplicationContext](./code/failednomatchingapplicationcontext.md)
  An error message that indicates there isn’t a matching app context for streaming.
### Invalid parameters
- [SCStreamError.Code.invalidParameter](./code/invalidparameter.md)
  An error message that indicates an operation failed because of an invalid parameter value.
### Creating an error
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
### Enumeration Cases
- [SCStreamError.Code.insufficientStorage](./code/insufficientstorage.md)
- [SCStreamError.Code.missingBackgroundMode](./code/missingbackgroundmode.md)
- [SCStreamError.Code.notSupported](./code/notsupported.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Stream errors (Objective-C)
- [SCStreamErrorDomain](../scstreamerrordomain.md)
  A string representation of the error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/code)*