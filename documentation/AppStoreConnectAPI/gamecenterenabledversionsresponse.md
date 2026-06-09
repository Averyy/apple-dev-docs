# GameCenterEnabledVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of app versions with Game Center enabled (deprecated; use GameCenterAppVersion).

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object GameCenterEnabledVersionsResponse
```

## Properties

- `data` ([GameCenterEnabledVersion]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterEnabledVersion](gamecenterenabledversion.md)
  An app version with Game Center enabled. Deprecated in API version 3.0; use [`GameCenterAppVersion`](gamecenterappversion.md) instead.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest](gamecenterenabledversioncompatibleversionslinkagesrequest.md)
  A request body you use to add or remove compatible versions from a Game Center-enabled version.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object AppGameCenterEnabledVersionsLinkagesResponse](appgamecenterenabledversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterenabledversionsresponse)*