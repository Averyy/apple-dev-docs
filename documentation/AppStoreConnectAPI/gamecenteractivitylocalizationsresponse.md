# GameCenterActivityLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of localizations for a Game Center activity.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterActivityLocalizationsResponse
```

## Properties

- `data` ([GameCenterActivityLocalization]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterActivityLocalization](gamecenteractivitylocalization.md)
  The localized name, description, and image for a Game Center activity in a specific language.
- [object GameCenterActivityLocalizationCreateRequest](gamecenteractivitylocalizationcreaterequest.md)
  The request body for creating a localization for a Game Center activity.
- [object GameCenterActivityLocalizationResponse](gamecenteractivitylocalizationresponse.md)
  A response containing a single localization for a Game Center activity.
- [object GameCenterActivityLocalizationUpdateRequest](gamecenteractivitylocalizationupdaterequest.md)
  The request body you use to update an activity localization.
- [object GameCenterActivityLocalizationImageLinkageResponse](gamecenteractivitylocalizationimagelinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivitylocalizationsresponse)*