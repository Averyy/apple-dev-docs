# Read Background Asset Upload File Information for a Background Asset Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about a background asset upload file for a specific background asset version.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssetVersions/{id}/backgroundAssetUploadFiles`

## Parameters

- `fields[backgroundAssetUploadFiles]` ([string])
- `limit` (integer)

## See Also

- [Read Background Asset Version App Store Releases Information.](get-v1-backgroundassetversionappstorereleases-_id_.md)
  Get the state of a background asset version App Store release.
- [Read Background Assets External Beta Release Information](get-v1-backgroundassetversionexternalbetareleases-_id_.md)
  Get the state of a background asset version external beta release.
- [Read Background Assets Internal Beta Release Information](get-v1-backgroundassetversioninternalbetareleases-_id_.md)
  Get the state of a background asset version internal beta release.
- [Read Background Assets Information](get-v1-backgroundassetversions-_id_.md)
  Get details about a specific background asset version.
- [Get the Background Asset Upload Files Resource ID for a Background Asset Version](get-v1-backgroundassetversions-_id_-relationships-backgroundassetuploadfiles.md)
  Get the ID for an uploaded asset pack Apple hosted background asset version


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles)*