# GameCenterAchievementReleasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list Game Center achievement releases.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterAchievementReleasesResponse
```

## Properties

- `data` ([GameCenterAchievementRelease]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterAchievementRelease](gamecenterachievementrelease.md)
  The data structure that represent an achievements release resource.
- [object GameCenterAchievementReleaseCreateRequest](gamecenterachievementreleasecreaterequest.md)
  The request body you use to create an achievement release.
- [object GameCenterAchievementReleaseResponse](gamecenterachievementreleaseresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center achievement release.
- [object GameCenterAchievementReleasesLinkagesResponse](gamecenterachievementreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterachievementreleasesresponse)*