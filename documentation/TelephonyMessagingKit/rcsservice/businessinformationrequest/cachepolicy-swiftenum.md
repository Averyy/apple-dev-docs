# RCSService.BusinessInformationRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum

`

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
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
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/businessinformationrequest/cachepolicy-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/businessinformationrequest/cachepolicy-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](rcsservice/businessinformationrequest/cachepolicy-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](rcsservice/businessinformationrequest/cachepolicy-swift.enum/hashvalue.md)
  The hash value.
### Comparing cache policies
- [static func == (RCSService.BusinessInformationRequest.CachePolicy, RCSService.BusinessInformationRequest.CachePolicy) -> Bool](rcsservice/businessinformationrequest/cachepolicy-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/businessinformationrequest/cachepolicy-swift.enum/equatable-implementations.md)

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