# GameCenterChallengesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a list of Game Center challenges configured for an app.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object GameCenterChallengesResponse
```

## Properties

- `data` ([GameCenterChallenge]) *(required)*
- `included` ([*]): **Allowed Types**: `GameCenterChallengeVersion`, `GameCenterDetail`, `GameCenterGroup`, `GameCenterLeaderboard`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object GameCenterChallenge](./gamecenterchallenge.md)
  The data structure that represent a challenge.
- [object GameCenterChallengeCreateRequest](./gamecenterchallengecreaterequest.md)
  The request body you use to create a challenge.
- [object GameCenterChallengeResponse](./gamecenterchallengeresponse.md)
  A response containing a single Game Center challenge configuration.
- [object GameCenterChallengeUpdateRequest](./gamecenterchallengeupdaterequest.md)
  The request body you use to update a challenge.
- [object GameCenterChallengeVersion](./gamecenterchallengeversion.md)
  The data structure that represent a challenge version.
- [object GameCenterChallengeVersionInlineCreate](./gamecenterchallengeversioninlinecreate.md)
  The data structure you use to configure a challenge version while creating a challenge.
- [object GameCenterChallengeVersionRelease](./gamecenterchallengeversionrelease.md)
  The data structure that represent a challenge version release.
- [object GameCenterChallengeLeaderboardV2LinkageRequest](./gamecenterchallengeleaderboardv2linkagerequest.md)
  The data structure that represents a Game Center challenge leaderboard linkage request resource.
- [object GameCenterChallengeLeaderboardLinkageRequest](./gamecenterchallengeleaderboardlinkagerequest.md)
- [object GameCenterChallengeVersionsLinkagesResponse](./gamecenterchallengeversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterchallengesresponse)*