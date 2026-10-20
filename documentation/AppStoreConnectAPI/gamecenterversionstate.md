# GameCenterVersionState

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

A string representing the state of a Game Center version.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```
string GameCenterVersionState
```

## Possible Values

- `PREPARE_FOR_SUBMISSION`
- `READY_FOR_REVIEW`
- `WAITING_FOR_REVIEW`
- `IN_REVIEW`
- `REJECTED`
- `ACCEPTED`
- `PENDING_RELEASE`
- `LIVE`
- `REPLACED_WITH_NEW_VERSION`
- `DEVELOPER_REJECTED`

## See Also

### Objects
- [object GameCenterAppVersion](./gamecenterappversion.md)
- [object GameCenterAppVersionCompatibilityVersionsLinkagesRequest](./gamecenterappversioncompatibilityversionslinkagesrequest.md)
  The request body you use to create a relationship between an app version and a compatibility version.
- [object GameCenterAppVersionCompatibilityVersionsLinkagesResponse](./gamecenterappversioncompatibilityversionslinkagesresponse.md)
  A response that confirms a relationship between an app version and a compatilibty version.
- [object GameCenterAppVersionCreateRequest](./gamecenterappversioncreaterequest.md)
  The request body you use to create an app version.
- [object GameCenterAppVersionResponse](./gamecenterappversionresponse.md)
  A response containing a single app version with its Game Center configuration.
- [object GameCenterAppVersionUpdateRequest](./gamecenterappversionupdaterequest.md)
  The request body you use to update an app version.
- [object GameCenterAppVersionsResponse](./gamecenterappversionsresponse.md)
  A response containing a list of app versions with Game Center enabled.
- [object GameCenterAppVersionAppStoreVersionLinkageResponse](./gamecenterappversionappstoreversionlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterversionstate)*