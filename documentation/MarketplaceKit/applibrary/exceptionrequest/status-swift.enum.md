# AppLibrary.ExceptionRequest.Status

**Framework**: MarketplaceKit  
**Kind**: enum  
**Role**: Enumeration

The possible statuses of an exception request for an app.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
enum Status
```

#### Overview

The [`AppLibrary.ExceptionRequest`](../exceptionrequest.md) structure’s [`status`](./status-swift.property.md) property is of this type.

## Topics

### Determining the status
- [AppLibrary.ExceptionRequest.Status.approved](./status-swift.enum/approved.md)
  A status that indicates the parent or guardian allows a specific app installation.
- [AppLibrary.ExceptionRequest.Status.declined](./status-swift.enum/declined.md)
  A status that indicates the parent or guardian disallows a specific app installation.
- [AppLibrary.ExceptionRequest.Status.pending](./status-swift.enum/pending.md)
  A status that indicates an app installation awaits the decision of a parent or guardian.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting the request status
- [let status: AppLibrary.ExceptionRequest.Status](./status-swift.property.md)
  A status that indicates the parent or guardian’s decision for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/exceptionrequest/status-swift.enum)*