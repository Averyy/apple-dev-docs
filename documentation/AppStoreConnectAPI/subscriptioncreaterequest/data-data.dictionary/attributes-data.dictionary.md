# SubscriptionCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a subscription create request resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object SubscriptionCreateRequest.Data.Attributes
```

## Mentions

- [Managing auto-renewable subscriptions](../../managing-auto-renewable-subscriptions.md)

## Properties

- `familySharable` (boolean)
- `name` (string) *(required)*
- `productId` (string) *(required)*
- `reviewNote` (string)
- `subscriptionPeriod` (string): **Allowed Values**: `ONE_WEEK`, `ONE_MONTH`, `TWO_MONTHS`, `THREE_MONTHS`, `SIX_MONTHS`, `ONE_YEAR`
- `groupLevel` (integer)

## See Also

### Objects
- [object SubscriptionCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptioncreaterequest/data-data.dictionary/attributes-data.dictionary)*