# GameCenterAchievementReleaseResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create, read, or modify a single Game Center achievement release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated.

## Declaration

```
object GameCenterAchievementReleaseResponse
```

## Properties

- `data` (GameCenterAchievementRelease) *(required)* *(deprecated)*
- `included` ([*]): **Allowed Types**: `GameCenterAchievement`, `GameCenterDetail`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object GameCenterAchievementRelease](./gamecenterachievementrelease.md)
  The data structure that represent an achievements release resource.
- [object GameCenterAchievementReleaseCreateRequest](./gamecenterachievementreleasecreaterequest.md)
  The request body you use to create an achievement release.
- [object GameCenterAchievementReleasesResponse](./gamecenterachievementreleasesresponse.md)
  The response body for endpoints that list Game Center achievement releases.
- [object GameCenterAchievementReleasesLinkagesResponse](./gamecenterachievementreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterachievementreleaseresponse)*