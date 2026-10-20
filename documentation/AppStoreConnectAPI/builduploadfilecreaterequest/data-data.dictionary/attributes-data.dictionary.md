# BuildUploadFileCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that you update for a build upload file resource.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```
object BuildUploadFileCreateRequest.Data.Attributes
```

## Properties

- `assetType` (string) *(required)*: **Allowed Values**: `ASSET`, `ASSET_DESCRIPTION`, `ASSET_SPI`
- `fileName` (string) *(required)*
- `fileSize` (int64) *(required)*: **Minimum**: `1`; **Maximum**: `9007199254740991`
- `uti` (string) *(required)*: **Allowed Values**: `com.apple.binary-property-list`, `com.apple.ipa`, `com.apple.pkg`, `com.apple.xml-property-list`, `com.pkware.zip-archive`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/builduploadfilecreaterequest/data-data.dictionary/attributes-data.dictionary)*