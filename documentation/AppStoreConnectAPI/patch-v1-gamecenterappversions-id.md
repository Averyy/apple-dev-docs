# Modify an app version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the state of Game Center enablement for an app version.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create an app version](post-v1-gamecenterappversions.md)
  Add a new Game Center app version.
- [Add compatible app version relationships](post-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Create a relationship between two Game Center app versions.
- [Remove compatible app version relationships](delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Remove a compatible version relationship from an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterappversions-_id_)*