# LiveAssistanceRequestError

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

An error thrown by a live assistance extension when handling a request.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
enum LiveAssistanceRequestError
```

## Overview

Throw this error from your implementations of [`prepareAssistanceRequest(_:)`](./liveassistanceextension/prepareassistancerequest%28_%29.md) and [`resumeRequest(_:)`](./liveassistanceextension/resumerequest%28_%29.md) to end requests that you can’t service.

Throwing is terminal; the request ends immediately, although the person using FaceTime can initiate a new one.

If your container app can resolve the situation by requesting further input, don’t throw an error. Instead, return [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](./liveassistancerequest/response/requiresuserinput%28reason%29.md) to give the person a chance to sign in or otherwise provide the needed information.

> **Note**:  This enumeration is not `frozen`. Code that switches over a `LiveAssistanceRequestError` must include an `@unknown default` block.

## Topics

### Working with errors
- [LiveAssistanceRequestError.cannotFulfill(message:)](./liveassistancerequesterror/cannotfulfill%28message%29.md)
  An error that indicates the extension can’t fulfill the request.
- [LiveAssistanceRequestError.unknown(message:)](./liveassistancerequesterror/unknown%28message%29.md)
  An error that indicates an unexpected failure prevented servicing the request.

## Relationships

### Conforms To
- [Error](../Swift/error.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with supporting types
- [struct LiveAssistanceRequest](./liveassistancerequest.md)
  A pending interpreter request, sent from the framework to the extension.
- [protocol LiveAssistanceExtensionConfiguration](./liveassistanceextensionconfiguration.md)
  An interface type required to conform to the ExtensionFoundation framework protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequesterror)*