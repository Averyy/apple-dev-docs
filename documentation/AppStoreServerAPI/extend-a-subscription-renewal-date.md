# Extend a Subscription Renewal Date

**Framework**: App Store Server API  
**Kind**: httpRequest

Extends the renewal date of a customer’s active subscription using the original transaction identifier.

**Availability**:
- App Store Server API 1.1+

## Mentions

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Identifying rate limits](identifying-rate-limits.md)
- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Use this endpoint to compensate your customers for temporary service outages, canceled events, or interruptions to live streamed events by extending the renewal date of their paid, active subscription. This endpoint acts on a single subscription for a transaction identifier that you specify.

To call this endpoint, provide the original transaction identifier of the subscription that experienced the service interruption. In the request body, [`ExtendRenewalDateRequest`](extendrenewaldaterequest.md), provide the extension duration, the reason code for the extension, and a unique [`requestIdentifier`](requestidentifier.md) for each extension request.

When this endpoint extends eligible purchased subscriptions that support Family Sharing, it automatically extends the family members’ subscriptions as well. However, the endpoint doesn’t support requests to extend a family member’s subscription directly.

A successful response with an `HTTP` `200` status code contains the [`ExtendRenewalDateResponse`](extendrenewaldateresponse.md) object. The response object includes the same unique request identifier you provide in the request, and information you need to determine whether the extension succeeds. For successful extensions, the new subscription expiration date is the [`effectiveDate`](effectivedate.md). All status codes other than `HTTP` `200` indicate that the request failed.

> **Note**:  After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

 After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

After a successful renewal date extension, Apple sends an email to notify the customer of their updated subscription renewal date.

For more information about this and related endpoints, including subscription eligibility, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## Request Body

The request body containing subscription-renewal-extension data.

## See Also

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)
  Compensate eligible active subscribers for service interruptions by extending a subscription’s renewal date.
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
- [object MassExtendRenewalDateStatusResponse](massextendrenewaldatestatusresponse.md)
  A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/extend-a-subscription-renewal-date)*