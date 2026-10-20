# GameCenterAchievementRelease

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data structure that represent an achievements release resource.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated.

## Declaration

```
object GameCenterAchievementRelease
```

## Topics

### Objects
- [object GameCenterAchievementRelease.Attributes](./gamecenterachievementrelease/attributes-data.dictionary.md)
  Attributes that describe a achievement resource.
- [object GameCenterAchievementRelease.Relationships](./gamecenterachievementrelease/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterAchievementRelease.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterAchievementRelease.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `gameCenterAchievementReleases`

## See Also

### Objects
- [object GameCenterAchievementReleaseCreateRequest](./gamecenterachievementreleasecreaterequest.md)
  The request body you use to create an achievement release.
- [object GameCenterAchievementReleaseResponse](./gamecenterachievementreleaseresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center achievement release.
- [object GameCenterAchievementReleasesResponse](./gamecenterachievementreleasesresponse.md)
  The response body for endpoints that list Game Center achievement releases.
- [object GameCenterAchievementReleasesLinkagesResponse](./gamecenterachievementreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterachievementrelease)*