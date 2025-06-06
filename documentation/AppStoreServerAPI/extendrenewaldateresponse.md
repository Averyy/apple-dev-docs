# ExtendRenewalDateResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that indicates whether an individual renewal-date extension succeeded, and related details.

**Availability**:
- App Store Server API 1.1+

## Declaration

```swift
object ExtendRenewalDateResponse
```

## Mentions

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)

#### Discussion

This object is the response data for the [`Extend a Subscription Renewal Date`](extend-a-subscription-renewal-date.md) endpoint.

## Topics

### Response data types
- [type effectiveDate](effectivedate.md)
  The new subscription expiration date for a subscription-renewal extension.
- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of a purchase.
- [type success](success.md)
  A Boolean value that indicates whether the subscription-renewal-date extension succeeded.
- [type webOrderLineItemId](weborderlineitemid.md)
  The unique identifier of subscription-purchase events across devices, including renewals.

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
- [object MassExtendRenewalDateRequest](massextendrenewaldaterequest.md)
  The request body that contains subscription-renewal-extension data to apply for all eligible active subscribers.
- [object MassExtendRenewalDateResponse](massextendrenewaldateresponse.md)
  A response that indicates the server successfully received the subscription-renewal-date extension request.
- [object MassExtendRenewalDateStatusResponse](massextendrenewaldatestatusresponse.md)
  A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/extendrenewaldateresponse)*