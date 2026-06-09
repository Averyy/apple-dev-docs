# Game Center Enabled Versions

**Framework**: App Store Connect API

Manage compatible Game Center-enabled versions.

#### Overview

Use a `gameCenterEnabledVersions` resource to indicate which versions of your app support Game Center. For more information see [`Game Center Configuration Guide for App Store Connect`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/overview-of-game-center).

## Topics

### Listing Versions
- [List all game center enabled versions for an app](get-v1-apps-_id_-gamecenterenabledversions.md)
  Get a list of Game Center enabled versions for a specific app.
- [List all compatible versions for a game center enabled version](get-v1-gamecenterenabledversions-_id_-compatibleversions.md)
### Getting and Adding Compatible Versions
- [Get all compatible version ids for a game center enabled version](get-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
- [Add compatible versions to a game center enabled version](post-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
### Removing and Replacing Compatible Versions
- [Replace all compatible versions for a game center enabled version](patch-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
- [Remove compatible versions from a game center enabled version](delete-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
### Objects
- [object GameCenterEnabledVersion](gamecenterenabledversion.md)
  An app version with Game Center enabled. Deprecated in API version 3.0; use [`GameCenterAppVersion`](gamecenterappversion.md) instead.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest](gamecenterenabledversioncompatibleversionslinkagesrequest.md)
  A request body you use to add or remove compatible versions from a Game Center-enabled version.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object GameCenterEnabledVersionsResponse](gamecenterenabledversionsresponse.md)
  A response containing a list of app versions with Game Center enabled (deprecated; use GameCenterAppVersion).
- [object AppGameCenterEnabledVersionsLinkagesResponse](appgamecenterenabledversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-enabled-versions)*