# LiveAssistanceRequesterPresenceObserving

**Framework**: LiveCommunicationKit  
**Kind**: protocol  
**Role**: Protocol

A live assistance extension that wants to know when the requester leaves or rejoins the call, or when the call ends.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
protocol LiveAssistanceRequesterPresenceObserving : LiveAssistanceExtension
```

## Overview

Adopt this protocol in the same type that adopts [`LiveAssistanceExtension`](./liveassistanceextension.md) when your service needs these changes, for example to release an interpreter after the requester leaves.

The framework only launches your extension for these changes if it adopts this protocol. It checks for the protocol when [`prepareAssistanceRequest(_:)`](./liveassistanceextension/prepareassistancerequest%28_%29.md) or [`resumeRequest(_:)`](./liveassistanceextension/resumerequest%28_%29.md) returns [`LiveAssistanceRequest.Response.proceed`](./liveassistancerequest/response/proceed.md).

The framework calls these methods only for requests that already reached your backend. Each `request` carries the same [`id`](./liveassistancerequest/id.md) and [`url`](./liveassistancerequest/url.md) your extension received then, so your backend can match the change to the interpreter session it started. In your implementation, forward the change to your backend.

The framework calls one method for each change, in the order the changes happen. It doesn’t retry the call, and the outcome doesn’t affect the request.

## Topics

### Observing requester presence
- [func requesterDidLeave(LiveAssistanceRequest) async](./liveassistancerequesterpresenceobserving/requesterdidleave%28_%29.md)
  Tells the extension that the person who made the request left the call.
- [func requesterDidRejoin(LiveAssistanceRequest) async](./liveassistancerequesterpresenceobserving/requesterdidrejoin%28_%29.md)
  Tells the extension that the person who made the request rejoined the call after leaving it.
### Observing call life cycle
- [func requestCallDidEnd(LiveAssistanceRequest) async](./liveassistancerequesterpresenceobserving/requestcalldidend%28_%29.md)
  Tells the extension that the call ended on the requester’s device, and the request ended with it.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)
- [LiveAssistanceExtension](./liveassistanceextension.md)

## See Also

### Conversation assistance
- [protocol LiveAssistanceExtension](./liveassistanceextension.md)
  The protocol you extend to provide live assistance services.
- [enum LiveAssistance](./liveassistance.md)
  A namespace to collect APIs for use by container apps that provide live assistance services.
- [Live assistance captioning](./liveassistancecaptioning.md)
  Use a WebSocket API to perform real-time captioning in a FaceTime call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequesterpresenceobserving)*