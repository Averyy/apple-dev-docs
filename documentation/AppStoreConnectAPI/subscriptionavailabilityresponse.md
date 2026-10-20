# SubscriptionAvailabilityResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single territory availability configuration for a subscription.

**Availability**:
- App Store Connect API 2.3+ - Deprecated in 4.4

> **Deprecated**: This object is deprecated.

## Declaration

```
object SubscriptionAvailabilityResponse
```

## Properties

- `data` (SubscriptionAvailability) *(required)* *(deprecated)*
- `included` ([Territory])
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object SubscriptionAvailability](./subscriptionavailability.md)
  The territory availability configuration for a subscription, specifying which App Store regions it’s offered in.
- [object SubscriptionAvailabilityCreateRequest](./subscriptionavailabilitycreaterequest.md)
  The request body you use to create a subscription availability.
- [object SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse](./subscriptionavailabilityavailableterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionavailabilityresponse)*