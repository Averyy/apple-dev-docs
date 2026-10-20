# BuildUploadFile.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a build upload file resource.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```
object BuildUploadFile.Attributes
```

## Properties

- `assetDeliveryState` (AppMediaAssetState)
- `assetToken` (string)
- `assetType` (string): **Allowed Values**: `ASSET`, `ASSET_DESCRIPTION`, `ASSET_SPI`
- `fileName` (string)
- `fileSize` (int64): **Minimum**: `1`; **Maximum**: `9007199254740991`
- `sourceFileChecksums` (Checksums)
- `uploadOperations` ([DeliveryFileUploadOperation])
- `uti` (string): **Allowed Values**: `com.apple.binary-property-list`, `com.apple.ipa`, `com.apple.pkg`, `com.apple.xml-property-list`, `com.pkware.zip-archive`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/builduploadfile/attributes-data.dictionary)*