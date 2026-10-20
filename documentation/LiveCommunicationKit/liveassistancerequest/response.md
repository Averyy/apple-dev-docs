# LiveAssistanceRequest.Response

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

A response from the extension to a live assistance request.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
enum Response
```

#### Overview

You return this type from your implementations of [`prepareAssistanceRequest(_:)`](../liveassistanceextension/prepareassistancerequest%28_%29.md) and [`resumeRequest(_:)`](../liveassistanceextension/resumerequest%28_%29.md) to express how the request should continue. Both cases are outcomes that indicate the request should continue. If the request can’t continue, your implementations of the protocol methods throws [`LiveAssistanceRequestError`](../liveassistancerequesterror.md) instead of returning a response.

> **Note**:  This enumeration is not `frozen`. Code that switches over a `Response` must include an `@unknown default` block.

## Topics

### Working with responses
- [LiveAssistanceRequest.Response.proceed](./response/proceed.md)
  A response that indicates the extension successfully handled the request and setting up live assistance can proceed.
- [case requiresUserInput(reason: LiveAssistanceLaunchReason)](./response/requiresuserinput%28reason%29.md)
  A response that indicates the extension needs to complete a task in the container app before the request can proceed.
- [enum LiveAssistanceLaunchReason](../liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequest/response)*