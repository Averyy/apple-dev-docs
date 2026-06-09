# GameCenterActivityVersionRelease

**Framework**: App Store Connect API  
**Kind**: dictionary

A record indicating that a version of a Game Center activity has been released to players.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterActivityVersionRelease
```

## Topics

### Dictionaries
- [object GameCenterActivityVersionRelease.Relationships](gamecenteractivityversionrelease/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterActivityVersionRelease.Relationships)
- `type` (string) *(required)*

## See Also

- [object GameCenterActivityVersionReleaseCreateRequest](gamecenteractivityversionreleasecreaterequest.md)
  The request body for releasing a Game Center activity version to players.
- [object GameCenterActivityVersionReleaseResponse](gamecenteractivityversionreleaseresponse.md)
  A response containing a single release record for a Game Center activity version.
- [object GameCenterActivityVersionReleasesResponse](gamecenteractivityversionreleasesresponse.md)
  A response containing a list of release records for a Game Center activity version.
- [object GameCenterActivityVersionResponse](gamecenteractivityversionresponse.md)
  A response containing a single version of a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivityversionrelease)*