# SubscriptionAvailability

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The territory availability configuration for a subscription, specifying which App Store regions it’s offered in.

**Availability**:
- App Store Connect API 2.3+ - Deprecated in 4.4

> **Deprecated**: This object is deprecated.

## Declaration

```
object SubscriptionAvailability
```

## Topics

### Objects
- [object SubscriptionAvailability.Attributes](./subscriptionavailability/attributes-data.dictionary.md)
  Attributes that describe a subscription availability resource.
- [object SubscriptionAvailability.Relationships](./subscriptionavailability/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionAvailability.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionAvailability.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `subscriptionAvailabilities`

## See Also

### Objects
- [object SubscriptionAvailabilityCreateRequest](./subscriptionavailabilitycreaterequest.md)
  The request body you use to create a subscription availability.
- [object SubscriptionAvailabilityResponse](./subscriptionavailabilityresponse.md)
  A response containing a single territory availability configuration for a subscription.
- [object SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse](./subscriptionavailabilityavailableterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionavailability)*