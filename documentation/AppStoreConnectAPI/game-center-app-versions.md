# Game Center app versions

**Framework**: App Store Connect API

Manage app versions for your apps.

## Topics

### Reading Game Center app versions
- [Read app versions for a Game Center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [GET /v1/gameCenterAppVersions/{id}](get-v1-gamecenterappversions-_id_.md)
  Read the Game Center enablement state and related app version information.
- [GET /v1/gameCenterAppVersions/{id}/appStoreVersion](get-v1-gamecenterappversions-_id_-appstoreversion.md)
  Read the app store version and related information for an app version.
- [GET /v1/gameCenterAppVersions/{id}/relationships/appStoreVersion](get-v1-gamecenterappversions-_id_-relationships-appstoreversion.md)
- [GET /v1/gameCenterAppVersions/{id}/compatibilityVersions](get-v1-gamecenterappversions-_id_-compatibilityversions.md)
  Get compatibility version information for a specific app version.
- [GET /v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions](get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.
### Creating, editing, and deleting Game Center app versions
- [POST /v1/gameCenterAppVersions](post-v1-gamecenterappversions.md)
  Add a new Game Center app version.
- [POST /v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions](post-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Create a relationship between two Game Center app versions.
- [PATCH /v1/gameCenterAppVersions/{id}](patch-v1-gamecenterappversions-_id_.md)
  Change the state of Game Center enablement for an app version.
- [DELETE /v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions](delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Remove a compatible version relationship from an app version.
### Objects
- [object GameCenterAppVersion](gamecenterappversion.md)
- [object GameCenterAppVersionCompatibilityVersionsLinkagesRequest](gamecenterappversioncompatibilityversionslinkagesrequest.md)
  The request body you use to create a relationship between an app version and a compatibility version.
- [object GameCenterAppVersionCompatibilityVersionsLinkagesResponse](gamecenterappversioncompatibilityversionslinkagesresponse.md)
  A response that confirms a relationship between an app version and a compatilibty version.
- [object GameCenterAppVersionCreateRequest](gamecenterappversioncreaterequest.md)
  The request body you use to create an app version.
- [object GameCenterAppVersionResponse](gamecenterappversionresponse.md)
  A response that contains a single app version resource.
- [object GameCenterAppVersionUpdateRequest](gamecenterappversionupdaterequest.md)
  The request body you use to update an app version.
- [object GameCenterAppVersionsResponse](gamecenterappversionsresponse.md)
  A response that contains a list of app version resources.
- [object GameCenterAppVersionAppStoreVersionLinkageResponse](gamecenterappversionappstoreversionlinkageresponse.md)
- [type GameCenterVersionState](gamecenterversionstate.md)
  A string representing the state of a Game Center version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-app-versions)*