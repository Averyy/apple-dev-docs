# GameCenterEnabledVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

An app version with Game Center enabled. Deprecated in API version 3.0; use [`GameCenterAppVersion`](gamecenterappversion.md) instead.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object GameCenterEnabledVersion
```

## Topics

### Objects
- [object GameCenterEnabledVersion.Attributes](gamecenterenabledversion/attributes-data.dictionary.md)
  Attributes that describe a Game Center Enabled Versions resource.
- [object GameCenterEnabledVersion.Relationships](gamecenterenabledversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterEnabledVersion.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterEnabledVersion.Relationships)
- `type` (string) *(required)*

## See Also

- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest](gamecenterenabledversioncompatibleversionslinkagesrequest.md)
  A request body you use to add or remove compatible versions from a Game Center-enabled version.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object GameCenterEnabledVersionsResponse](gamecenterenabledversionsresponse.md)
  A response containing a list of app versions with Game Center enabled (deprecated; use GameCenterAppVersion).
- [object AppGameCenterEnabledVersionsLinkagesResponse](appgamecenterenabledversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterenabledversion)*