# RCSService.BusinessInformationRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum

`

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum CachePolicy
```

#### Overview

The cache policy used for a business information request.

## Topics

### Inspecting cache policies
- [RCSService.BusinessInformationRequest.CachePolicy.cacheOnly](rcsservice/businessinformationrequest/cachepolicy-swift.enum/cacheonly.md)
  Load from local cache.
- [RCSService.BusinessInformationRequest.CachePolicy.remoteOnly](rcsservice/businessinformationrequest/cachepolicy-swift.enum/remoteonly.md)
  Load from remote.
- [RCSService.BusinessInformationRequest.CachePolicy.cacheOrRemote](rcsservice/businessinformationrequest/cachepolicy-swift.enum/cacheorremote.md)
  Load from local cache if available, otherwise load from remote.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/businessinformationrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle.URI](rcsservice/businessinformationrequest/handle.md)
  URI handle of the target.
- [var cachePolicy: RCSService.BusinessInformationRequest.CachePolicy](rcsservice/businessinformationrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/businessinformationrequest/cachepolicy-swift.enum)*