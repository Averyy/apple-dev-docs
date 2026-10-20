# SubscriptionUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a subscription update request resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object SubscriptionUpdateRequest.Data.Attributes
```

## Properties

- `familySharable` (boolean)
- `name` (string)
- `reviewNote` (string)
- `subscriptionPeriod` (string): **Allowed Values**: `ONE_WEEK`, `ONE_MONTH`, `TWO_MONTHS`, `THREE_MONTHS`, `SIX_MONTHS`, `ONE_YEAR`
- `groupLevel` (integer)
- `marketSettings` ([string]): The markets in which the subscription is available for multi-seat purchase.

  **Allowed Values**: `APPLE_SCHOOL`, `APP_STORE`, `APPLE_BUSINESS`
- `multiSeatStatus` (string): The status that indicates whether the subscription supports multiple seats for organizations. Turning on Family Sharing for the subscription automatically sets this value to DISABLED.

  **Allowed Values**: `ENABLED`, `DISABLED`

## See Also

### Objects
- [object SubscriptionUpdateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionupdaterequest/data-data.dictionary/attributes-data.dictionary)*