# AppLibrary.ExceptionRequest

**Framework**: MarketplaceKit  
**Kind**: struct

A structure that describes an app that a person requests permission to install.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
struct ExceptionRequest
```

#### Overview

When a person tries to install an app with an age rating beyond the maximum allowed for the device (see [`maximumAllowedAgeRating`](applibrary/maximumallowedagerating.md)), the framework tracks the request by adding an instance of this structure to the [`currentAgeExceptionRequests()`](applibrary/currentageexceptionrequests().md) list.

For more information, see [`Providing age-rating appropriate content`](providing-age-rating-appropriate-content.md).

## Topics

### Identifying the requested app
- [let appleItemID: AppleItemID](applibrary/exceptionrequest/appleitemid.md)
  An identifier for the app that requires an age-rating exception.
### Inspecting the request status
- [let status: AppLibrary.ExceptionRequest.Status](applibrary/exceptionrequest/status-swift.property.md)
  A status that indicates the parent or guardian’s decision for the request.
- [AppLibrary.ExceptionRequest.Status](applibrary/exceptionrequest/status-swift.enum.md)
  The possible statuses of an exception request for an app.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var maximumAllowedAgeRating: Int](applibrary/maximumallowedagerating.md)
  An age rating that specifies the maximum rating set for content on the device.
- [func currentAgeExceptionRequests() async throws -> [AppLibrary.ExceptionRequest]](applibrary/currentageexceptionrequests.md)
  Returns a list of requests to install apps that exceed the maximum allowed age rating for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/exceptionrequest)*