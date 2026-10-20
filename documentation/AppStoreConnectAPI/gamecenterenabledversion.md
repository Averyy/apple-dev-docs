# GameCenterEnabledVersion

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

An app version with Game Center enabled. Deprecated in API version 3.0; use [`GameCenterAppVersion`](./gamecenterappversion.md) instead.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This object is deprecated. Use [`GameCenterAppVersion`](./gamecenterappversion.md) instead.

## Declaration

```
object GameCenterEnabledVersion
```

## Topics

### Objects
- [object GameCenterEnabledVersion.Attributes](./gamecenterenabledversion/attributes-data.dictionary.md)
  Attributes that describe a Game Center Enabled Versions resource.
- [object GameCenterEnabledVersion.Relationships](./gamecenterenabledversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterEnabledVersion.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterEnabledVersion.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `gameCenterEnabledVersions`

## See Also

### Objects
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest](./gamecenterenabledversioncompatibleversionslinkagesrequest.md)
  A request body you use to add or remove compatible versions from a Game Center-enabled version.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](./gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object GameCenterEnabledVersionsResponse](./gamecenterenabledversionsresponse.md)
  A response containing a list of app versions with Game Center enabled (deprecated; use GameCenterAppVersion).
- [object AppGameCenterEnabledVersionsLinkagesResponse](./appgamecenterenabledversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterenabledversion)*