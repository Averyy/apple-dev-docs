# streamDidBecomeInactive(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func streamDidBecomeInactive(_ stream: SCStream)
```

```objc
- (void) streamDidBecomeInactive:(SCStream *) stream;
```

#### Discussion

streamDidBecomeInactive:

notifies the delegate that all the windows that are currently being shared are exited. This callback occurs for all content filter types.

## Parameters

- `stream`: The SCStream object


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/streamdidbecomeinactive(_:))*