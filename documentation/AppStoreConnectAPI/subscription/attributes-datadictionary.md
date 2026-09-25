# Subscription.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a subscription resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object Subscription.Attributes
```

## Properties

- `familySharable` (boolean)
- `name` (string)
- `productId` (string)
- `reviewNote` (string)
- `state` (string)
- `subscriptionPeriod` (string)
- `groupLevel` (integer)
- `marketSettings` ([string]): The markets in which the subscription is available for multi-seat purchase.
- `multiSeatStatus` (string): The status that indicates whether the subscription supports multiple seats for organizations. Turning on Family Sharing for the subscription automatically sets this value to DISABLED.

## See Also

- [object Subscription.Relationships](subscription/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription/attributes-data.dictionary)*