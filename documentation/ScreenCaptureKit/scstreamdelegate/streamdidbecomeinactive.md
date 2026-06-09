# streamDidBecomeInactive(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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