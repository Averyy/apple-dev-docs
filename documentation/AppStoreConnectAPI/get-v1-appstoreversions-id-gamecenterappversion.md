# Read game center app version information of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the status of Game Center enablement for an App Store version.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/gameCenterAppVersion`

## Parameters

- `fields[appStoreVersions]` ([string])
- `include` ([string])
- `fields[gameCenterAppVersions]` ([string])
- `limit[compatibilityVersions]` (integer)

## See Also

- [Get the Game Center app version ID for an App Store version](get-v1-appstoreversions-_id_-relationships-gamecenterappversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-gamecenterappversion)*