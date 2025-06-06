# Get Status of Subscription Renewal Date Extensions

**Framework**: App Store Server API  
**Kind**: httpRequest

Checks whether a renewal date extension request completed, and provides the final count of successful or failed extensions.

**Availability**:
- App Store Server API 1.7+

## Mentions

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This endpoint provides basic status information about a request you initiate when you call the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint. Such requests may take hours, or even days, depending on the number of subscribers. This status tells whether the request is complete. If so, it has the total count of successful and failed subscription-renewal-date extensions.

> 💡 **Tip**:  If you don’t need this status on demand, or need more details, use the [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications) for near real-time status information instead. For more information about related notifications, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

 If you don’t need this status on demand, or need more details, use the [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications) for near real-time status information instead. For more information about related notifications, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## See Also

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
  Compensate eligible active subscribers for service interruptions by extending a subscription’s renewal date.
- [Extend a Subscription Renewal Date](extend-a-subscription-renewal-date.md)
  Extends the renewal date of a customer’s active subscription using the original transaction identifier.
- [Extend Subscription Renewal Dates for All Active Subscribers](extend-subscription-renewal-dates-for-all-active-subscribers.md)
  Uses a subscription’s product identifier to extend the renewal date for all of its eligible active subscribers.
- [object ExtendRenewalDateRequest](extendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data for an individual subscription.
- [object ExtendRenewalDateResponse](extendrenewaldateresponse.md)
  A response that indicates whether an individual renewal-date extension succeeded, and related details.
- [object MassExtendRenewalDateRequest](massextendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data to apply for all eligible active subscribers.
- [object MassExtendRenewalDateResponse](massextendrenewaldateresponse.md)
  A response that indicates the server successfully received the subscription-renewal-date extension request.
- [object MassExtendRenewalDateStatusResponse](massextendrenewaldatestatusresponse.md)
  A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-status-of-subscription-renewal-date-extensions)*