# GameCenterActivityLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The localized name, description, and image for a Game Center activity in a specific language.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object GameCenterActivityLocalization
```

## Topics

### Dictionaries
- [object GameCenterActivityLocalization.Attributes](./gamecenteractivitylocalization/attributes-data.dictionary.md)
  Attributes that describe an activity resource.
- [object GameCenterActivityLocalization.Relationships](./gamecenteractivitylocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterActivityLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterActivityLocalization.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `gameCenterActivityLocalizations`

## See Also

### Objects
- [object GameCenterActivityLocalizationCreateRequest](./gamecenteractivitylocalizationcreaterequest.md)
  The request body for creating a localization for a Game Center activity.
- [object GameCenterActivityLocalizationResponse](./gamecenteractivitylocalizationresponse.md)
  A response containing a single localization for a Game Center activity.
- [object GameCenterActivityLocalizationUpdateRequest](./gamecenteractivitylocalizationupdaterequest.md)
  The request body you use to update an activity localization.
- [object GameCenterActivityLocalizationsResponse](./gamecenteractivitylocalizationsresponse.md)
  A response containing a list of localizations for a Game Center activity.
- [object GameCenterActivityLocalizationImageLinkageResponse](./gamecenteractivitylocalizationimagelinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivitylocalization)*