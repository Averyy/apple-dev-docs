# GameCenterEnabledVersionCompatibleVersionsLinkagesRequest

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A request body you use to add or remove compatible versions from a Game Center-enabled version.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This object is deprecated. Use [`GameCenterAppVersionCompatibilityVersionsLinkagesRequest`](./gamecenterappversioncompatibilityversionslinkagesrequest.md) instead.

## Declaration

```
object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest
```

## Topics

### Objects
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.Data](./gamecenterenabledversioncompatibleversionslinkagesrequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` ([GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.Data]) *(required)*

## See Also

### Objects
- [object GameCenterEnabledVersion](./gamecenterenabledversion.md)
  An app version with Game Center enabled. Deprecated in API version 3.0; use [`GameCenterAppVersion`](./gamecenterappversion.md) instead.
- [object GameCenterEnabledVersionCompatibleVersionsLinkagesResponse](./gamecenterenabledversioncompatibleversionslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object GameCenterEnabledVersionsResponse](./gamecenterenabledversionsresponse.md)
  A response containing a list of app versions with Game Center enabled (deprecated; use GameCenterAppVersion).
- [object AppGameCenterEnabledVersionsLinkagesResponse](./appgamecenterenabledversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterenabledversioncompatibleversionslinkagesrequest)*