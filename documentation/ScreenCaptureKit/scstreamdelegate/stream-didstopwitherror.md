# stream(_:didStopWithError:)

**Framework**: Screencapturekit  
**Kind**: method

Tells the delegate that the stream stopped with an error.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
optional func stream(_ stream: SCStream, didStopWithError error: any Error)
```

#### Discussion

> **Note**:  When the `error` parameter has the code [`SCStreamError.Code.userStopped`](scstreamerror/code/userstopped.md), the user took an intentional action to cancel the stream. Treat errors of this type as expected and recoverable failures.

## Parameters

- `stream`: The stream that stopped.
- `error`: The error that caused the stream stoppage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/stream(_:didstopwitherror:))*