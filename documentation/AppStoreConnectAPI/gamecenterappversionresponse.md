# GameCenterAppVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single app version with its Game Center configuration.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```
object GameCenterAppVersionResponse
```

## Properties

- `data` (GameCenterAppVersion) *(required)*
- `included` ([*]): **Allowed Types**: `AppStoreVersion`, `GameCenterAppVersion`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object GameCenterAppVersion](./gamecenterappversion.md)
- [object GameCenterAppVersionCompatibilityVersionsLinkagesRequest](./gamecenterappversioncompatibilityversionslinkagesrequest.md)
  The request body you use to create a relationship between an app version and a compatibility version.
- [object GameCenterAppVersionCompatibilityVersionsLinkagesResponse](./gamecenterappversioncompatibilityversionslinkagesresponse.md)
  A response that confirms a relationship between an app version and a compatilibty version.
- [object GameCenterAppVersionCreateRequest](./gamecenterappversioncreaterequest.md)
  The request body you use to create an app version.
- [object GameCenterAppVersionUpdateRequest](./gamecenterappversionupdaterequest.md)
  The request body you use to update an app version.
- [object GameCenterAppVersionsResponse](./gamecenterappversionsresponse.md)
  A response containing a list of app versions with Game Center enabled.
- [object GameCenterAppVersionAppStoreVersionLinkageResponse](./gamecenterappversionappstoreversionlinkageresponse.md)
- [type GameCenterVersionState](./gamecenterversionstate.md)
  A string representing the state of a Game Center version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterappversionresponse)*