# GameCenterAppVersionCompatibilityVersionsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that confirms a relationship between an app version and a compatilibty version.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterAppVersionCompatibilityVersionsLinkagesResponse
```

## Topics

### Objects
- [object GameCenterAppVersionCompatibilityVersionsLinkagesResponse.Data](gamecenterappversioncompatibilityversionslinkagesresponse/data-data.dictionary.md)
  The type and ID of a related Game Center app version resource.

## Properties

- `data` ([GameCenterAppVersionCompatibilityVersionsLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterAppVersion](gamecenterappversion.md)
- [object GameCenterAppVersionCompatibilityVersionsLinkagesRequest](gamecenterappversioncompatibilityversionslinkagesrequest.md)
  The request body you use to create a relationship between an app version and a compatibility version.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterappversioncompatibilityversionslinkagesresponse)*