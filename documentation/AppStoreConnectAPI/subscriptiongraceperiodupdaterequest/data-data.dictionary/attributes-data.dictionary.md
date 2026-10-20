# SubscriptionGracePeriodUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a subscription grace period update request resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object SubscriptionGracePeriodUpdateRequest.Data.Attributes
```

## Mentions

- [Managing auto-renewable subscriptions](../../managing-auto-renewable-subscriptions.md)

## Properties

- `duration` (SubscriptionGracePeriodDuration): [`SubscriptionGracePeriodDuration`](../../subscriptiongraceperiodduration.md)
- `optIn` (boolean)
- `renewalType` (string): **Allowed Values**: `ALL_RENEWALS`, `PAID_TO_PAID_ONLY`
- `sandboxOptIn` (boolean)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongraceperiodupdaterequest/data-data.dictionary/attributes-data.dictionary)*