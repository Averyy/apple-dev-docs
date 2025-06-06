# failedNoMatchingApplicationContext

**Framework**: ScreenCaptureKit  
**Kind**: property

An error message that indicates there isn’t a matching app context for streaming.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static var failedNoMatchingApplicationContext: SCStreamError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror/failednomatchingapplicationcontext)*