# GameCenterEnabledVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a list of app versions with Game Center enabled (deprecated; use GameCenterAppVersion).

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This object is deprecated. Use [`GameCenterAppVersionsResponse`](./gamecenterappversionsresponse.md) instead.

## Declaration

```
object GameCenterEnabledVersionsResponse
```

## Properties

- `data` ([GameCenterEnabledVersion]) *(required)*
- `included` ([*]): **Allowed Types**: `App`, `GameCenterEnabledVersion`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object GameCenterEnabledVersion](./gamecenterenabledversion.md)
  An app version with Game Center enabled. Deprecated in API version 3.0; use [`GameCenterAppVersion`](./gamecenterappversion.md) instead.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest](./gamecenterenabledversioncompatibleversionslinkagesrequest.md)
  A request body you use to add or remove compatible versions from a Game Center-enabled version.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](./gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object AppGameCenterEnabledVersionsLinkagesResponse](./appgamecenterenabledversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterenabledversionsresponse)*