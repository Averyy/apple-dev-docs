# RCSService.BusinessInformationRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure representing a request to retrieve information about a business.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct BusinessInformationRequest
```

#### Overview

To create an instance of this type, use the [`CellularServiceID`](cellularserviceid.md) and [`RCSHandle`](rcshandle.md) from an [`RCSMessage`](rcsmessage.md) you receive in the RCS service’s [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md). Then call [`businessInformation(for:)`](rcsservice/businessinformation(for:).md) on the RCS service, which returns an instance of the [`RCSService.Business`](rcsservice/business.md) type.

## Topics

### Creating a business information request
- [init(cellularServiceID: CellularServiceID, handle: RCSHandle.URI, cachePolicy: RCSService.BusinessInformationRequest.CachePolicy)](rcsservice/businessinformationrequest/init(cellularserviceid:handle:cachepolicy:).md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](rcsservice/businessinformationrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle.URI](rcsservice/businessinformationrequest/handle.md)
  URI handle of the target.
- [var cachePolicy: RCSService.BusinessInformationRequest.CachePolicy](rcsservice/businessinformationrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.
- [RCSService.BusinessInformationRequest.CachePolicy](rcsservice/businessinformationrequest/cachepolicy-swift.enum.md)
  `

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func businessInformation(for: RCSService.BusinessInformationRequest) async throws -> RCSService.Business?](rcsservice/businessinformation(for:).md)
  Requests business information for a specified handle.
- [RCSService.Business](rcsservice/business.md)
  Structure containing details about a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/businessinformationrequest)*