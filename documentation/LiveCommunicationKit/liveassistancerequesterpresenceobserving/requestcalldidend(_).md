# requestCallDidEnd(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the extension that the call ended on the requester’s device, and the request ended with it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
func requestCallDidEnd(_ request: LiveAssistanceRequest) async
```

## Discussion

The framework calls this once, even if it already called [`requesterDidLeave(_:)`](./requesterdidleave%28_%29.md). It doesn’t call any of these methods again for this request.

## Parameters

- `request`: The request whose call ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequesterpresenceobserving/requestcalldidend(_:))*