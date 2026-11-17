# requesterDidRejoin(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the extension that the person who made the request rejoined the call after leaving it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
func requesterDidRejoin(_ request: LiveAssistanceRequest) async
```

## Parameters

- `request`: The request whose requester rejoined the call.

## See Also

### Observing requester presence
- [func requesterDidLeave(LiveAssistanceRequest) async](./requesterdidleave%28_%29.md)
  Tells the extension that the person who made the request left the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequesterpresenceobserving/requesterdidrejoin(_:))*