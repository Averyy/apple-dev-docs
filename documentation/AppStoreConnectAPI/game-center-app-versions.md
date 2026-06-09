# Game Center app versions

**Framework**: App Store Connect API

Manage app versions for your apps.

## Topics

### Reading Game Center app versions
- [Read app versions for a game center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [List Game Center app version IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [Read app version information](get-v1-gamecenterappversions-_id_.md)
  Read the Game Center enablement state and related app version information.
- [Read the App Store version for an app version](get-v1-gamecenterappversions-_id_-appstoreversion.md)
  Read the App Store version and related information for an app version.
- [Get the App Store version ID for a Game Center app version](get-v1-gamecenterappversions-_id_-relationships-appstoreversion.md)
- [Read compatibility version information](get-v1-gamecenterappversions-_id_-compatibilityversions.md)
  Get compatibility version information for a specific app version.
- [List all compatible app version IDs](get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.
### Creating, editing, and deleting Game Center app versions
- [Create an app version](post-v1-gamecenterappversions.md)
  Add a new Game Center app version.
- [Add compatible app version relationships](post-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Create a relationship between two Game Center app versions.
- [Modify an app version](patch-v1-gamecenterappversions-_id_.md)
  Change the state of Game Center enablement for an app version.
- [Remove compatible app version relationships](delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
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
  A response containing a single app version with its Game Center configuration.
- [object GameCenterAppVersionUpdateRequest](gamecenterappversionupdaterequest.md)
  The request body you use to update an app version.
- [object GameCenterAppVersionsResponse](gamecenterappversionsresponse.md)
  A response containing a list of app versions with Game Center enabled.
- [object GameCenterAppVersionAppStoreVersionLinkageResponse](gamecenterappversionappstoreversionlinkageresponse.md)
- [type GameCenterVersionState](gamecenterversionstate.md)
  A string representing the state of a Game Center version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-app-versions)*