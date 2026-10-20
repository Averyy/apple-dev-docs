# InAppPurchaseImageCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create a subscription purchase image reservation.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`InAppPurchaseImageV2CreateRequest`](../inapppurchaseimagev2createrequest.md) instead.

## Declaration

```
object InAppPurchaseImageCreateRequest.Data
```

## Topics

### Objects
- [object InAppPurchaseImageCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a subscription purchase image request resource.
- [object InAppPurchaseImageCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (InAppPurchaseImageCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (InAppPurchaseImageCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `inAppPurchaseImages`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimagecreaterequest/data-data.dictionary)*