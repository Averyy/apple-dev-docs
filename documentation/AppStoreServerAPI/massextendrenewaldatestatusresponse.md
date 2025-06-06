# MassExtendRenewalDateStatusResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
object MassExtendRenewalDateStatusResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The App Store server sends this response when you call the [`Get Status of Subscription Renewal Date Extensions`](get-status-of-subscription-renewal-date-extensions.md) endpoint. Your request to [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) is complete when the value of the `complete` field is `TRUE`. Otherwise, the request is still in progress.

The App Store server also sends real-time notifications as it’s processing the subscription-renewal-date extension, including notifications with [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) values of `RENEWAL_EXTENSION` and `RENEWAL_EXTENDED`. For more information, see [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications). For more information about extending subscription renewal dates, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## Topics

### Data types
- [type complete](complete.md)
  A Boolean value that indicates whether the App Store completed the request to extend a subscription renewal date to active subscribers.
- [type completeDate](completedate.md)
  The UNIX time, in milliseconds, that the App Store completes a request to extend a subscription renewal date for eligible subscribers.
- [type failedCount](failedcount.md)
  The count of subscriptions that fail to receive a subscription-renewal-date extension.
- [type succeededCount](succeededcount.md)
  The count of subscriptions that successfully receive a subscription-renewal-date extension.

## See Also

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
  Compensate eligible active subscribers for service interruptions by extending a subscription’s renewal date.
- [Extend a Subscription Renewal Date](extend-a-subscription-renewal-date.md)
  Extends the renewal date of a customer’s active subscription using the original transaction identifier.
- [Extend Subscription Renewal Dates for All Active Subscribers](extend-subscription-renewal-dates-for-all-active-subscribers.md)
  Uses a subscription’s product identifier to extend the renewal date for all of its eligible active subscribers.
- [Get Status of Subscription Renewal Date Extensions](get-status-of-subscription-renewal-date-extensions.md)
  Checks whether a renewal date extension request completed, and provides the final count of successful or failed extensions.
- [object ExtendRenewalDateRequest](extendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data for an individual subscription.
- [object ExtendRenewalDateResponse](extendrenewaldateresponse.md)
  A response that indicates whether an individual renewal-date extension succeeded, and related details.
- [object MassExtendRenewalDateRequest](massextendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data to apply for all eligible active subscribers.
- [object MassExtendRenewalDateResponse](massextendrenewaldateresponse.md)
  A response that indicates the server successfully received the subscription-renewal-date extension request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/massextendrenewaldatestatusresponse)*