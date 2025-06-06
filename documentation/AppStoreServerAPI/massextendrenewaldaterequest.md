# MassExtendRenewalDateRequest

**Framework**: App Store Server API  
**Kind**: dictionary

The request body that contains subscription-renewal-extension data to apply for all eligible active subscribers.

**Availability**:
- App Store Server API 1.7+

## Declaration

```swift
object MassExtendRenewalDateRequest
```

## Mentions

- [Extending the renewal date for auto-renewable subscriptions](extending-the-renewal-date-for-auto-renewable-subscriptions.md)

#### Discussion

This request body applies to the [`Extend Subscription Renewal Dates for All Active Subscribers`](extend-subscription-renewal-dates-for-all-active-subscribers.md) endpoint.

The `requestIdentifier` uniquely identifies this request. Use the same `requestIdentifier` in the following APIs :

- The [`Get Status of Subscription Renewal Date Extensions`](get-status-of-subscription-renewal-date-extensions.md) endpoint
- The [`summary`](https://developer.apple.com/documentation/AppStoreServerNotifications/summary) object in [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications).

For more information, see [`Extending the renewal date for auto-renewable subscriptions`](extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## Topics

### Data types
- [type extendByDays](extendbydays.md)
  The number of days to extend the subscription renewal date.
- [type extendReasonCode](extendreasoncode.md)
  The code that represents the reason for the subscription-renewal-date extension.
- [string productId](../AppStoreServerNotifications/productId.md)
  The product identifier of the In-App Purchase.
- [type requestIdentifier](requestidentifier.md)
  A string that contains a unique identifier you provide to track each subscription-renewal-date extension request.
- [type storefrontCountryCode](storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront.
- [type storefrontCountryCodes](storefrontcountrycodes.md)
  A list of storefront country codes you provide to limit the storefronts for a subscription-renewal-date extension.

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
- [object MassExtendRenewalDateResponse](massextendrenewaldateresponse.md)
  A response that indicates the server successfully received the subscription-renewal-date extension request.
- [object MassExtendRenewalDateStatusResponse](massextendrenewaldatestatusresponse.md)
  A response that indicates the current status of a request to extend the subscription renewal date to all eligible subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/massextendrenewaldaterequest)*