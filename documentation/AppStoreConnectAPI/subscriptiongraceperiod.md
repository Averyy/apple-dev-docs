# SubscriptionGracePeriod

**Framework**: App Store Connect API  
**Kind**: dictionary

A grace period configuration for a subscription, allowing subscribers continued access while payment issues are resolved.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionGracePeriod
```

## Topics

### Objects
- [object SubscriptionGracePeriod.Attributes](subscriptiongraceperiod/attributes-data.dictionary.md)
  Attributes that describe a subscription grace period resource.

## Properties

- `attributes` (SubscriptionGracePeriod.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [type SubscriptionGracePeriodDuration](subscriptiongraceperiodduration.md)
  A string that represents the grace period duration for a subscription.
- [object SubscriptionGracePeriodResponse](subscriptiongraceperiodresponse.md)
  A response containing a single grace period configuration for a subscription.
- [object SubscriptionGracePeriodUpdateRequest](subscriptiongraceperiodupdaterequest.md)
  The request body you use to update a subscription grace period update request.
- [object AppSubscriptionGracePeriodLinkageResponse](appsubscriptiongraceperiodlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongraceperiod)*