# LiveAssistanceRequestError

**Framework**: LiveCommunicationKit  
**Kind**: enum

An error thrown by a live assistance extension when handling a request.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum LiveAssistanceRequestError
```

#### Overview

Throw this error from your implementations of [`prepareAssistanceRequest(_:)`](liveassistanceextension/prepareassistancerequest(_:).md) and [`resumeRequest(_:)`](liveassistanceextension/resumerequest(_:).md) to end requests that you can’t service.

Throwing is terminal; the request ends immediately, although the person using FaceTime can initiate a new one.

If your container app can resolve the situation by requesting further input, don’t throw an error. Instead, return [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](liveassistancerequest/response/requiresuserinput(reason:).md) to give the person a chance to sign in or otherwise provide the needed information.

> **Note**:  This enumeration is not `frozen`. Code that switches over a `LiveAssistanceRequestError` must include an `@unknown default` block.

## Topics

### Working with errors
- [LiveAssistanceRequestError.cannotFulfill(message:)](liveassistancerequesterror/cannotfulfill(message:).md)
  An error that indicates the extension can’t fulfill the request.
- [LiveAssistanceRequestError.unknown(message:)](liveassistancerequesterror/unknown(message:).md)
  An error that indicates an unexpected failure prevented servicing the request.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct LiveAssistanceRequest](liveassistancerequest.md)
  A pending interpreter request, sent from the framework to the extension.
- [protocol LiveAssistanceExtensionConfiguration](liveassistanceextensionconfiguration.md)
  An interface type required to conform to the ExtensionFoundation framework protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequesterror)*