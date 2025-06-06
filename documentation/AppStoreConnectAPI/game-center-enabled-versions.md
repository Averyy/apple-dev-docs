# Game Center Enabled Versions

**Framework**: App Store Connect API

Manage compatible game center-enabled versions.

#### Overview

Use a `gameCenterEnabledVersions` resource to indicate which versions of your app support Game Center. For more information see [`Game Center Configuration Guide for App Store Connect`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/overview-of-game-center).

## Topics

### Listing Versions
- [List All Game Center Enabled Versions for an App](get-v1-apps-_id_-gamecenterenabledversions.md)
- [List All Compatible Versions for a Game Center Enabled Version](get-v1-gamecenterenabledversions-_id_-compatibleversions.md)
### Getting and Adding Compatible Versions
- [Get All Compatible Version IDs for a Game Center Enabled Version](get-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
- [Add Compatible Versions to a Game Center Enabled Version](post-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
### Removing and Replacing Compatible Versions
- [Replace All Compatible Versions for a Game Center Enabled Version](patch-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
- [Remove Compatible Versions from a Game Center Enabled Version](delete-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)
### Objects
- [object GameCenterEnabledVersion](gamecenterenabledversion.md)
  The data structure that represents the Game Center Enabled Versions resource.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest](gamecenterenabledversioncompatibleversionslinkagesrequest.md)
  A request body you use to add or remove compatible versions from a Game Center-enabled version.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object GameCenterEnabledVersionsResponse](gamecenterenabledversionsresponse.md)
  A response that contains a list of Game Center Enabled Version resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-enabled-versions)*