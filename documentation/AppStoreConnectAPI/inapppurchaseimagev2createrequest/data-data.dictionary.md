# InAppPurchaseImageV2CreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an In-App Purchase image with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```
object InAppPurchaseImageV2CreateRequest.Data
```

## Topics

### Objects
- [object InAppPurchaseImageV2CreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe an In-App Purchase image create request resource.
- [object InAppPurchaseImageV2CreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: **Allowed Values**: `inAppPurchaseImages`
- `attributes` (InAppPurchaseImageV2CreateRequest.Data.Attributes) *(required)*
- `relationships` (InAppPurchaseImageV2CreateRequest.Data.Relationships) *(required)*


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimagev2createrequest/data-data.dictionary)*