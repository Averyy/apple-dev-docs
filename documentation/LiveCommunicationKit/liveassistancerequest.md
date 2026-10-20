# LiveAssistanceRequest

**Framework**: LiveCommunicationKit  
**Kind**: struct  
**Role**: Structure

A pending interpreter request, sent from the framework to the extension.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
struct LiveAssistanceRequest
```

#### Overview

This is a value type sent by the framework to the request. All properties are read-only.

## Topics

### Working with request properties
- [let id: UUID](./liveassistancerequest/id.md)
  A unique identifier that relates the request to a conversation in the FaceTime framework.
- [let url: URL](./liveassistancerequest/url.md)
  The FaceTime-generated URL for this request.
### Working with supporting types
- [LiveAssistanceRequest.Response](./liveassistancerequest/response.md)
  A response from the extension to a live assistance request.

## Relationships

### Conforms To
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with supporting types
- [enum LiveAssistanceRequestError](./liveassistancerequesterror.md)
  An error thrown by a live assistance extension when handling a request.
- [protocol LiveAssistanceExtensionConfiguration](./liveassistanceextensionconfiguration.md)
  An interface type required to conform to the ExtensionFoundation framework protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequest)*