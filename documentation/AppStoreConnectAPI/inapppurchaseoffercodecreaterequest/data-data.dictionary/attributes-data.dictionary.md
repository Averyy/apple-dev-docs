# InAppPurchaseOfferCodeCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an In-App Purchase offer code create request.

**Availability**:
- App Store Connect API 4.2+

## Declaration

```
object InAppPurchaseOfferCodeCreateRequest.Data.Attributes
```

## Properties

- `customerEligibilities` ([string]) *(required)*: **Allowed Values**: `NON_SPENDER`, `ACTIVE_SPENDER`, `CHURNED_SPENDER`
- `name` (string) *(required)*

## See Also

### Dictionaries
- [object InAppPurchaseOfferCodeCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseoffercodecreaterequest/data-data.dictionary/attributes-data.dictionary)*