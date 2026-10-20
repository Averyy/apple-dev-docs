# InAppPurchaseLocalizationV2CreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an In-App Purchase localization with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```
object InAppPurchaseLocalizationV2CreateRequest.Data
```

## Topics

### Objects
- [object InAppPurchaseLocalizationV2CreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe an In-App Purchase localization create request resource.
- [object InAppPurchaseLocalizationV2CreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: **Allowed Values**: `inAppPurchaseLocalizations`
- `attributes` (InAppPurchaseLocalizationV2CreateRequest.Data.Attributes) *(required)*
- `relationships` (InAppPurchaseLocalizationV2CreateRequest.Data.Relationships) *(required)*


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalizationv2createrequest/data-data.dictionary)*