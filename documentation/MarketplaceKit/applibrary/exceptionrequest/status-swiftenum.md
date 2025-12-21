# AppLibrary.ExceptionRequest.Status

**Framework**: MarketplaceKit  
**Kind**: enum

The possible statuses of an exception request for an app.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
enum Status
```

#### Overview

The [`AppLibrary.ExceptionRequest`](applibrary/exceptionrequest.md) structure’s [`status`](applibrary/exceptionrequest/status-swift.property.md) property is of this type.

## Topics

### Determining the status
- [AppLibrary.ExceptionRequest.Status.approved](applibrary/exceptionrequest/status-swift.enum/approved.md)
  A status that indicates the parent or guardian allows a specific app installation.
- [AppLibrary.ExceptionRequest.Status.declined](applibrary/exceptionrequest/status-swift.enum/declined.md)
  A status that indicates the parent or guardian disallows a specific app installation.
- [AppLibrary.ExceptionRequest.Status.pending](applibrary/exceptionrequest/status-swift.enum/pending.md)
  A status that indicates an app installation awaits the decision of a parent or guardian.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let status: AppLibrary.ExceptionRequest.Status](applibrary/exceptionrequest/status-swift.property.md)
  A status that indicates the parent or guardian’s decision for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/exceptionrequest/status-swift.enum)*