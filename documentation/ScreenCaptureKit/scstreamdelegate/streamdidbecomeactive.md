# streamDidBecomeActive(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- Mac Catalyst 18.2+
- macOS 15.2+

## Declaration

```swift
optional func streamDidBecomeActive(_ stream: SCStream)
```

#### Discussion

streamDidBecomeActive:

notifies the delegate the first time any window that was being shared in the stream is re-opened after all the windows being shared are closed.  When all the windows being shared are closed, the client will receive streamDidBecomeInactive:.

## Parameters

- `stream`: The SCStream object


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/streamdidbecomeactive(_:))*