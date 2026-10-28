# Read Release Information for an Achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read the state of an achievement release and related information.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/4a6bcd3d-0325-418b-3bbf-671bd15be8c6/releases
```

**Response**:

```json
{
  “data” : [ {
    “type” : “gameCenterAchievementReleases”,
    “id” : “be3bd01f-fd78-9093-63a7-bc25ff890eb2”,
    “attributes” : {
      “live” : true
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/be3bd01f-fd78-9093-63a7-bc25ff890eb2”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/4a6bcd3d-0325-418b-3bbf-671bd15be8c6/releases”
  },
  “meta” : {
    “paging” : {
      “total” : 1,
      “limit” : 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}/releases`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the achievements resource ID from the [`List All Achievements`](./get-v1-gamecenterdetails-_id_-gamecenterachievements.md) response.

### Query Parameters

- `fields[gameCenterAchievementReleases]` ([string]): **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterAchievement`
- `fields[gameCenterAchievements]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `points`, `showBeforeEarned`, `repeatable`, `archived`, `activityProperties`, `gameCenterDetail`, `gameCenterGroup`, `groupAchievement`, `localizations`, `releases`, `activity`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `filter[gameCenterDetail]` ([string])
- `filter[live]` ([string])
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterAchievement`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterAchievementReleasesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center achievement releases
- [List achievement releases](./get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [List release IDs for a Game Center achievement](./get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [Read game center achievement release information](./get-v1-gamecenterachievementreleases-_id_.md)
  Read the state of a specific achievement release.
- [Create a game center achievement release](./post-v1-gamecenterachievementreleases.md)
  Create a release for an achievement and a Game Center detail.
- [Delete a game center achievement release](./delete-v1-gamecenterachievementreleases-_id_.md)
  Delete a release of an achievement or Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievements-_id_-releases)*