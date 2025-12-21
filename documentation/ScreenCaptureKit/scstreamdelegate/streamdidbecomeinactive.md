# streamDidBecomeInactive(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- Mac Catalyst 18.2+
- macOS 15.2+

## Declaration

```swift
optional func streamDidBecomeInactive(_ stream: SCStream)
```

#### Discussion

streamDidBecomeInactive:

notifies the delegate that all the windows that are currently being shared are exited. This callback occurs for all content filter types.

## Parameters

- `stream`: The SCStream object


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/streamdidbecomeinactive(_:))*