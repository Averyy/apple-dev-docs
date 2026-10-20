# InAppPurchaseImageUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to update an In-App Purchase image.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`InAppPurchaseImageV2UpdateRequest`](../inapppurchaseimagev2updaterequest.md) instead.

## Declaration

```
object InAppPurchaseImageUpdateRequest.Data
```

## Topics

### Objects
- [object InAppPurchaseImageUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a subscription purchase image request resource.

## Properties

- `attributes` (InAppPurchaseImageUpdateRequest.Data.Attributes): The resource’s attributes.
- `id` (string) *(required)*
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `inAppPurchaseImages`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimageupdaterequest/data-data.dictionary)*