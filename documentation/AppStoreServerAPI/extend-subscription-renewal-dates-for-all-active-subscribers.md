# Extend Subscription Renewal Dates for All Active Subscribers

**Framework**: App Store Server API  
**Kind**: httpRequest

Uses a subscription’s product identifier to extend the renewal date for all of its eligible active subscribers.

**Availability**:
- App Store Server API 1.7+

## Mentions

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Use this endpoint to compensate your customers for temporary service outages, canceled events, or interruptions to live streamed events by extending the renewal date of their paid, active subscription. This endpoint acts on all active subscriptions for the product identifier you specify, and is limited to the storefronts you optionally specify.

To call this endpoint, provide the subscription product identifier that experienced the service interruption, and other information, in the request body, [`MassExtendRenewalDateRequest`](massextendrenewaldaterequest.md).

A successful response with an `HTTP 200` status code contains the [`MassExtendRenewalDateResponse`](massextendrenewaldateresponse.md) object, which includes the same unique `requestIdentifier` you provide in the request. This endpoint is an asynchronous request. A successful response indicates that the App Store server is processing the request. Status codes other than `HTTP 200` indicate that the request failed.

> **Note**:  After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

 After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

After a successful renewal date extension, Apple sends an email to notify the customer of their updated subscription renewal date.

For more information about this endpoint, including subscription eligibility, getting status notifications, and retrying extensions that fail, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## Request Body

The request body for extending a subscription renewal date for all of its active subscribers.

## See Also

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
  Compensate eligible active subscribers for service interruptions by extending a subscription’s renewal date.
- [Extend a Subscription Renewal Date](extend-a-subscription-renewal-date.md)
  Extends the renewal date of a customer’s active subscription using the original transaction identifier.
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
- [object MassExtendRenewalDateStatusResponse](massextendrenewaldatestatusresponse.md)
  A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/extend-subscription-renewal-dates-for-all-active-subscribers)*