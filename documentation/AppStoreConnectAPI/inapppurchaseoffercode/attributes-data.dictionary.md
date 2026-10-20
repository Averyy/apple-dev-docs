# InAppPurchaseOfferCode.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an In-App Purchase offer code resource.

**Availability**:
- App Store Connect API 4.2+

## Declaration

```
object InAppPurchaseOfferCode.Attributes
```

## Properties

- `active` (boolean)
- `customerEligibilities` ([string]): **Allowed Values**: `NON_SPENDER`, `ACTIVE_SPENDER`, `CHURNED_SPENDER`
- `name` (string)
- `productionCodeCount` (integer)
- `sandboxCodeCount` (integer)

## See Also

### Dictionaries
- [object InAppPurchaseOfferCode.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseoffercode/attributes-data.dictionary)*