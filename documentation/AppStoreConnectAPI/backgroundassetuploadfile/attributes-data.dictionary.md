# BackgroundAssetUploadFile.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a background asset upload file resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object BackgroundAssetUploadFile.Attributes
```

## Properties

- `assetDeliveryState` (AppMediaAssetState)
- `assetToken` (string)
- `assetType` (string): **Allowed Values**: `ASSET`, `MANIFEST`
- `fileName` (string)
- `fileSize` (int64): **Minimum**: `1`; **Maximum**: `9007199254740991`
- `sourceFileChecksum` (string) *(deprecated)*: This attribute is deprecated, use `sourceFileChecksums` instead.
- `sourceFileChecksums` (Checksums)
- `uploadOperations` ([DeliveryFileUploadOperation])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/backgroundassetuploadfile/attributes-data.dictionary)*