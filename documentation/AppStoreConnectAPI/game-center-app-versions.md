# Game Center app versions

**Framework**: App Store Connect API

Manage app versions for your apps.

## Topics

### Reading Game Center app versions
- [Read app versions for a Game Center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [Read information for a specific app version](get-v1-gamecenterappversions-_id_.md)
  Read the Game Center enablement state and related app version information.
- [Read the App Store version for an app version](get-v1-gamecenterappversions-_id_-appstoreversion.md)
  Read the app store version and related information for an app version.
- [Read compatibility version information](get-v1-gamecenterappversions-_id_-compatibilityversions.md)
  Get compatibility version information for a specific app version.
- [Read compatible app versions](get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.
### Creating, editing, and deleting Game Center app versions
- [Create an app version](post-v1-gamecenterappversions.md)
  Add a new Game Center app version.
- [Create a compatiblity relationship](post-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Create a relationship between two Game Center app versions.
- [Modify an app version](patch-v1-gamecenterappversions-_id_.md)
  Change the state of Game Center enablement for an app version.
- [Remove a compatilibly version](delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Remove a compatilible version relationship from an app version.
### Objects
- [object GameCenterAppVersion](gamecenterappversion.md)
  The data structure that represents a Game Center app version resource.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-app-versions)*