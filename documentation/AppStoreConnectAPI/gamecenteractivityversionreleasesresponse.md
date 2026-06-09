# GameCenterActivityVersionReleasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of release records for a Game Center activity version.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterActivityVersionReleasesResponse
```

## Properties

- `data` ([GameCenterActivityVersionRelease]) *(required)*
- `included` ([GameCenterActivityVersion])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterActivityVersionRelease](gamecenteractivityversionrelease.md)
  A record indicating that a version of a Game Center activity has been released to players.
- [object GameCenterActivityVersionReleaseCreateRequest](gamecenteractivityversionreleasecreaterequest.md)
  The request body for releasing a Game Center activity version to players.
- [object GameCenterActivityVersionReleaseResponse](gamecenteractivityversionreleaseresponse.md)
  A response containing a single release record for a Game Center activity version.
- [object GameCenterActivityVersionResponse](gamecenteractivityversionresponse.md)
  A response containing a single version of a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivityversionreleasesresponse)*