# BackgroundAssetUploadFile.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a background asset upload file resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object BackgroundAssetUploadFile.Attributes
```

## Properties

- `assetDeliveryState` (AppMediaAssetState)
- `assetToken` (string)
- `assetType` (string)
- `fileName` (string)
- `fileSize` (int64)
- `sourceFileChecksum` (string): This attribute is deprecated, use `sourceFileChecksums` instead.
- `sourceFileChecksums` (Checksums)
- `uploadOperations` ([DeliveryFileUploadOperation])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/backgroundassetuploadfile/attributes-data.dictionary)*