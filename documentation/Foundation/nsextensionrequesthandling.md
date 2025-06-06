# NSExtensionRequestHandling

**Framework**: Foundation  
**Kind**: protocol

The interface an app extension uses to respond to a request from a host app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSExtensionRequestHandling : NSObjectProtocol
```

#### Overview

The [`NSExtensionRequestHandling`](nsextensionrequesthandling.md) protocol provides a life cycle hook into an app extension. An extension’s principal object can implement this protocol and use [`beginRequest(with:)`](nsextensionrequesthandling/beginrequest(with:).md) to keep track of the request from a host app.

## Topics

### Preparing for a request
- [func beginRequest(with: NSExtensionContext)](nsextensionrequesthandling/beginrequest(with:).md)
  Tells the extension to prepare for a host app’s request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSExtensionContext](nsextensioncontext.md)
  The host app context from which an app extension is invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionrequesthandling)*