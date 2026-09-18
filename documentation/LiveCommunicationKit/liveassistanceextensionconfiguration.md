# LiveAssistanceExtensionConfiguration

**Framework**: LiveCommunicationKit  
**Kind**: protocol

An interface type required to conform to the ExtensionFoundation framework protocols.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
@preconcurrency protocol LiveAssistanceExtensionConfiguration : AppExtensionConfiguration
```

#### Overview

Your app doesn’t interact directly with this type.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../extensionfoundation/appextensionconfiguration.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct LiveAssistanceRequest](liveassistancerequest.md)
  A pending interpreter request, sent from the framework to the extension.
- [enum LiveAssistanceRequestError](liveassistancerequesterror.md)
  An error thrown by a live assistance extension when handling a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistanceextensionconfiguration)*