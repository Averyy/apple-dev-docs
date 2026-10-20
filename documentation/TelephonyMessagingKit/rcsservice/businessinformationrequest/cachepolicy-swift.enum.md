# RCSService.BusinessInformationRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

`

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum CachePolicy
```

#### Overview

The cache policy used for a business information request.

## Topics

### Inspecting cache policies
- [RCSService.BusinessInformationRequest.CachePolicy.cacheOnly](./cachepolicy-swift.enum/cacheonly.md)
  Load from local cache.
- [RCSService.BusinessInformationRequest.CachePolicy.remoteOnly](./cachepolicy-swift.enum/remoteonly.md)
  Load from remote.
- [RCSService.BusinessInformationRequest.CachePolicy.cacheOrRemote](./cachepolicy-swift.enum/cacheorremote.md)
  Load from local cache if available, otherwise load from remote.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing request properties
- [var cellularServiceID: CellularServiceID](./cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle.URI](./handle.md)
  URI handle of the target.
- [var cachePolicy: RCSService.BusinessInformationRequest.CachePolicy](./cachepolicy-swift.property.md)
  Cache policy to use for request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/businessinformationrequest/cachepolicy-swift.enum)*