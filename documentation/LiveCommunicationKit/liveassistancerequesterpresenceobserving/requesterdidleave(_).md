# requesterDidLeave(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the extension that the person who made the request left the call.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
func requesterDidLeave(_ request: LiveAssistanceRequest) async
```

## Discussion

The framework calls this whenever the requester leaves, including when they hang up. Release the interpreter promptly so the call can end. If the call ended, [`requestCallDidEnd(_:)`](./requestcalldidend%28_%29.md) follows.

## Parameters

- `request`: The request whose requester left the call.

## See Also

### Observing requester presence
- [func requesterDidRejoin(LiveAssistanceRequest) async](./requesterdidrejoin%28_%29.md)
  Tells the extension that the person who made the request rejoined the call after leaving it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequesterpresenceobserving/requesterdidleave(_:))*