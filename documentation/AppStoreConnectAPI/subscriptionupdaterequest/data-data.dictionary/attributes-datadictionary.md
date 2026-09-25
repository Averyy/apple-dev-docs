# SubscriptionUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a subscription update request resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionUpdateRequest.Data.Attributes
```

## Properties

- `familySharable` (boolean)
- `name` (string)
- `reviewNote` (string)
- `subscriptionPeriod` (string)
- `groupLevel` (integer)
- `marketSettings` ([string]): The markets in which the subscription is available for multi-seat purchase.
- `multiSeatStatus` (string): The status that indicates whether the subscription supports multiple seats for organizations. Turning on Family Sharing for the subscription automatically sets this value to DISABLED.

## See Also

- [object SubscriptionUpdateRequest.Data.Relationships](subscriptionupdaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionupdaterequest/data-data.dictionary/attributes-data.dictionary)*