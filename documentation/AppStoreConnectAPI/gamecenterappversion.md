# GameCenterAppVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object GameCenterAppVersion
```

## Topics

### Dictionaries
- [object GameCenterAppVersion.Attributes](gamecenterappversion/attributes-data.dictionary.md)
  Attributes that describe a Game Center app version resource.
- [object GameCenterAppVersion.Relationships](gamecenterappversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterAppVersion.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterAppVersion.Relationships)
- `type` (string) *(required)*

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterappversion)*