# requestIdentifier

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

A string that contains a unique identifier you provide to track a request, such as a subscription-renewal-date extension or a seat claim.

**Availability**:
- App Store Server API 1.1+

## Declaration

```
string requestIdentifier
```



**Maximum Length**: `128`

## Discussion

You provide a `requestIdentifier` in the request body when you call the [`Extend Subscription Renewal Dates for All Active Subscribers`](./extend-subscription-renewal-dates-for-all-active-subscribers.md), [`Extend a Subscription Renewal Date`](./extend-a-subscription-renewal-date.md), and [`Claim Seat`](./claim-seat.md) endpoints.

For the subscription-renewal-date extension endpoints, the API returns the same request identifier in its response, so you can match your request with the related response. The [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) also include this request identifier in notifications related to the [`Extend Subscription Renewal Dates for All Active Subscribers`](./extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint. For more information, see the `RENEWAL_EXTENSION` [`notificationType`](../AppStoreServerNotifications/notificationtype.md).

For the [`Claim Seat`](./claim-seat.md) endpoint, generate a new `requestIdentifier` for each claim, and save it before you call the endpoint. If you retry a request with the same `requestIdentifier` and the original request claimed a seat, the endpoint returns that seat claim rather than claiming another seat.

> ❗ **Important**:  Provide a `UUID` value for the [`requestIdentifier`](./requestidentifier.md) when calling the [`Extend Subscription Renewal Dates for All Active Subscribers`](./extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint.

The maximum string length is 128 characters.

To resend a request after a timeout or other error, use the same request identifier. Otherwise, create a unique request identifier for each request.

## See Also

### Request data types
- [type extendByDays](./extendbydays.md)
  The number of days to extend the subscription renewal date.
- [type extendReasonCode](./extendreasoncode.md)
  The code that represents the reason for the subscription-renewal-date extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/requestidentifier)*