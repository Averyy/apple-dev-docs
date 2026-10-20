# currentAgeExceptionRequests()

**Framework**: MarketplaceKit  
**Kind**: method  
**Role**: Instance Method

Returns a list of requests to install apps that exceed the maximum allowed age rating for the device.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
nonisolated
final func currentAgeExceptionRequests() async throws -> [AppLibrary.ExceptionRequest]
```

## Mentions

- [Providing age-rating appropriate content](../providing-age-rating-appropriate-content.md)

#### Discussion

When a person attempts to install an app with an age rating that exceeds the maximum allowed for the device, the framework presents a sheet that enables the person to request an exception from a parent or guardian. When the person proceeds with the request, the framework adds an instance of [`AppLibrary.ExceptionRequest`](./exceptionrequest.md) for the app to this list.

The parent or guardian reviews the request in Messages on their device, or in person on the originating device, by responding to a system-provided sheet. After the parent or guardian makes a decision, the framework removes the app’s [`AppLibrary.ExceptionRequest`](./exceptionrequest.md) from this list.

Keep the person informed of the [`status`](./exceptionrequest/status-swift.property.md) of the current exception requests. For example, if the exception status is [`AppLibrary.ExceptionRequest.Status.pending`](./exceptionrequest/status-swift.enum/pending.md), you can show a Pending label in place of an Install button for the associated app.

For more information, see [Providing age-rating appropriate content](../providing-age-rating-appropriate-content.md).

## See Also

### Checking for age-rating based content restrictions
- [var maximumAllowedAgeRating: Int](./maximumallowedagerating.md)
  An age rating that specifies the maximum rating set for content on the device.
- [AppLibrary.ExceptionRequest](./exceptionrequest.md)
  A structure that describes an app that a person requests permission to install.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/currentageexceptionrequests())*