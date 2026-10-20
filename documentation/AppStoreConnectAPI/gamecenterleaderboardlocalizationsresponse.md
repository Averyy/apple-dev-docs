# GameCenterLeaderboardLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list Game Center leaderboard localizations.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated. Use [`GameCenterLeaderboardLocalizationsV2Response`](./gamecenterleaderboardlocalizationsv2response.md) instead.

## Declaration

```
object GameCenterLeaderboardLocalizationsResponse
```

## Properties

- `data` ([GameCenterLeaderboardLocalization]) *(required)*
- `included` ([*]): **Allowed Types**: `GameCenterLeaderboardImage`, `GameCenterLeaderboard`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object GameCenterLeaderboardLocalizationV2](./gamecenterleaderboardlocalizationv2.md)
  The data structure that represents a Game Center leaderboard localization v2 resource.
- [object GameCenterLeaderboardLocalizationV2CreateRequest](./gamecenterleaderboardlocalizationv2createrequest.md)
  The request body you use to create a Game Center leaderboard localization v2.
- [object GameCenterLeaderboardLocalizationV2Response](./gamecenterleaderboardlocalizationv2response.md)
  A response that contains a single Game Center leaderboard localization v2 resource.
- [object GameCenterLeaderboardLocalizationV2UpdateRequest](./gamecenterleaderboardlocalizationv2updaterequest.md)
  The request body you use to update a Game Center leaderboard localization v2.
- [object GameCenterLeaderboardLocalizationsV2Response](./gamecenterleaderboardlocalizationsv2response.md)
  A response that contains a single Game Center leaderboard localization v2 resource.
- [object GameCenterLeaderboardLocalizationV2ImageLinkageResponse](./gamecenterleaderboardlocalizationv2imagelinkageresponse.md)
  A response that contains a single Game Center leaderboard localization v2 image linkage resource.
- [object GameCenterLeaderboardLocalization](./gamecenterleaderboardlocalization.md)
  The data structure that represent a leaderboard localization.
- [object GameCenterLeaderboardLocalizationCreateRequest](./gamecenterleaderboardlocalizationcreaterequest.md)
  The request body you use to create a leaderboard localization.
- [object GameCenterLeaderboardLocalizationResponse](./gamecenterleaderboardlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center leaderboard localization.
- [object GameCenterLeaderboardLocalizationUpdateRequest](./gamecenterleaderboardlocalizationupdaterequest.md)
  The request body you use to update a leaderboard localization.
- [object GameCenterLeaderboardLocalizationGameCenterLeaderboardImageLinkageResponse](./gamecenterleaderboardlocalizationgamecenterleaderboardimagelinkageresponse.md)
- [object GameCenterLeaderboardLocalizationsLinkagesResponse](./gamecenterleaderboardlocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardlocalizationsresponse)*