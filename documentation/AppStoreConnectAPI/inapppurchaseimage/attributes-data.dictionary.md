# InAppPurchaseImage.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a subscription image resource.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`InAppPurchaseImageV2`](../inapppurchaseimagev2.md) instead.

## Declaration

```
object InAppPurchaseImage.Attributes
```

## Properties

- `assetToken` (string)
- `fileName` (string)
- `fileSize` (integer)
- `imageAsset` (ImageAsset)
- `sourceFileChecksum` (string)
- `state` (string): **Allowed Values**: `AWAITING_UPLOAD`, `UPLOAD_COMPLETE`, `FAILED`, `PREPARE_FOR_SUBMISSION`, `WAITING_FOR_REVIEW`, `APPROVED`, `REJECTED`
- `uploadOperations` ([UploadOperation])

## See Also

### Objects
- [object InAppPurchaseImage.Relationships](./relationships-data.dictionary.md)
  The relationships for an In-App Purchase image, linking it to its associated In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseimage/attributes-data.dictionary)*