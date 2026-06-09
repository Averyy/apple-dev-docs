# SubscriptionAvailability

**Framework**: App Store Connect API  
**Kind**: dictionary

The territory availability configuration for a subscription, specifying which App Store regions it’s offered in.

**Availability**:
- App Store Connect API 2.3+

## Declaration

```swift
object SubscriptionAvailability
```

## Topics

### Objects
- [object SubscriptionAvailability.Attributes](subscriptionavailability/attributes-data.dictionary.md)
  Attributes that describe a subscription availability resource.
- [object SubscriptionAvailability.Relationships](subscriptionavailability/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionAvailability.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionAvailability.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionAvailabilityCreateRequest](subscriptionavailabilitycreaterequest.md)
  The request body you use to create a subscription availability.
- [object SubscriptionAvailabilityResponse](subscriptionavailabilityresponse.md)
  A response containing a single territory availability configuration for a subscription.
- [object SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse](subscriptionavailabilityavailableterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionavailability)*