# RCSService.BusinessInformationRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure representing a request to retrieve information about a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct BusinessInformationRequest
```

## Overview

To create an instance of this type, use the [`CellularServiceID`](../cellularserviceid.md) and [`RCSHandle`](../rcshandle.md) from an [`RCSMessage`](../rcsmessage.md) you receive in the RCS service’s [`incomingMessageNotifications`](./incomingmessagenotifications.md). Then call [`businessInformation(for:)`](./businessinformation%28for%29.md) on the RCS service, which returns an instance of the [`RCSService.Business`](./business.md) type.

## Topics

### Creating a business information request
- [init(cellularServiceID: CellularServiceID, handle: RCSHandle.URI, cachePolicy: RCSService.BusinessInformationRequest.CachePolicy)](./businessinformationrequest/init%28cellularserviceid,handle,cachepolicy%29.md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](./businessinformationrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle.URI](./businessinformationrequest/handle.md)
  URI handle of the target.
- [var cachePolicy: RCSService.BusinessInformationRequest.CachePolicy](./businessinformationrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.
- [RCSService.BusinessInformationRequest.CachePolicy](./businessinformationrequest/cachepolicy-swift.enum.md)
  `
### Structures
- [RCSService.BusinessInformationRequest.WelcomeMessageInformation](./businessinformationrequest/welcomemessageinformation-swift.struct.md)
### Instance Properties
- [var welcomeMessageInformation: RCSService.BusinessInformationRequest.WelcomeMessageInformation?](./businessinformationrequest/welcomemessageinformation-swift.property.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving business information
- [func businessInformation(for: RCSService.BusinessInformationRequest) async throws -> RCSService.Business?](./businessinformation%28for%29.md)
  Requests business information for a specified handle.
- [RCSService.Business](./business.md)
  Structure containing details about a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/businessinformationrequest)*