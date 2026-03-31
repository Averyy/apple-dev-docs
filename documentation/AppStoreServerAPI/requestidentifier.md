# requestIdentifier

**Framework**: App Store Server API  
**Kind**: typealias

A string that contains a unique identifier you provide to track each subscription-renewal-date extension request.

**Availability**:
- App Store Server API 1.1+

## Declaration

```swift
string requestIdentifier
```

#### Discussion

You provide a `requestIdentifier` in the request body when you call the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) and [`Extend a Subscription Renewal Date`](extend-a-subscription-renewal-date.md) endpoints.

The API returns the same request identifier in its response, so you can match your request with the related response. The [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) also include this request identifier in notifications related to the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint. For more information, see the `RENEWAL_EXTENSION` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType).

To resend the same request due to a timeout or other error, use the same request identifier. Otherwise, create a unique request identifer for each different subscription-renewal-date extension request.

> ❗ **Important**:  Provide a `UUID` value for the [`requestIdentifier`](requestidentifier.md) when calling the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint.

The maximum string length is 128 characters.

## See Also

- [type extendByDays](extendbydays.md)
  The number of days to extend the subscription renewal date.
- [type extendReasonCode](extendreasoncode.md)
  The code that represents the reason for the subscription-renewal-date extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/requestidentifier)*