# SubscriptionImage.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a subscription image resource.

**Availability**:
- App Store Connect API 3.6+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`SubscriptionImageV2`](../subscriptionimagev2.md) instead.

## Declaration

```
object SubscriptionImage.Attributes
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
- [object SubscriptionImage.Relationships](./relationships-data.dictionary.md)
  The relationships for a subscription image, linking it to its associated subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionimage/attributes-data.dictionary)*