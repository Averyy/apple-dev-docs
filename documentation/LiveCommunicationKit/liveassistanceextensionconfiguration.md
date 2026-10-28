# LiveAssistanceExtensionConfiguration

**Framework**: LiveCommunicationKit  
**Kind**: protocol  
**Role**: Protocol

An interface type required to conform to the ExtensionFoundation framework protocols.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
@MainActor
@preconcurrency protocol LiveAssistanceExtensionConfiguration : AppExtensionConfiguration
```

## Overview

Your app doesn’t interact directly with this type.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/appextensionconfiguration.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with supporting types
- [struct LiveAssistanceRequest](./liveassistancerequest.md)
  A pending interpreter request, sent from the framework to the extension.
- [enum LiveAssistanceRequestError](./liveassistancerequesterror.md)
  An error thrown by a live assistance extension when handling a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistanceextensionconfiguration)*