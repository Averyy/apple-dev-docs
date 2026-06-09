# GameCenterActivityVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of versions for a Game Center activity.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterActivityVersionsResponse
```

## Properties

- `data` ([GameCenterActivityVersion]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterActivityVersion](gamecenteractivityversion.md)
  A versioned configuration of a Game Center activity, containing its localizations and release status.
- [object GameCenterActivityVersionCreateRequest](gamecenteractivityversioncreaterequest.md)
  The request body for creating a version of a Game Center activity.
- [object GameCenterActivityVersionResponse](gamecenteractivityversionresponse.md)
  A response containing a single version of a Game Center activity.
- [object GameCenterActivityVersionUpdateRequest](gamecenteractivityversionupdaterequest.md)
  The request body you use to update an activity version version.
- [object GameCenterActivityVersionDefaultImageLinkageResponse](gamecenteractivityversiondefaultimagelinkageresponse.md)
- [object GameCenterActivityVersionLocalizationsLinkagesResponse](gamecenteractivityversionlocalizationslinkagesresponse.md)
- [object GameCenterActivityVersionUpdateRequest](gamecenteractivityversionupdaterequest.md)
  The request body you use to update an activity version version.
- [object GameCenterActivityVersionsLinkagesResponse](gamecenteractivityversionslinkagesresponse.md)
  A response containing the resource identifiers of versions for a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivityversionsresponse)*