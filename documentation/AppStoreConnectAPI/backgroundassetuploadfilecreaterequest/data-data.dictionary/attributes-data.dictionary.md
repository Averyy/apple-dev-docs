# BackgroundAssetUploadFileCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a background asset upload file create request resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object BackgroundAssetUploadFileCreateRequest.Data.Attributes
```

## Properties

- `assetType` (string) *(required)*:

  - **`ASSET`**: the .aar file that contains your background assets
  - **`MANIFEST`**: The manifest you generate to describe the .aar file.

  **Allowed Values**: `ASSET`, `MANIFEST`
- `fileName` (string) *(required)*
- `fileSize` (int64) *(required)*: **Minimum**: `1`; **Maximum**: `9007199254740991`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/backgroundassetuploadfilecreaterequest/data-data.dictionary/attributes-data.dictionary)*