# Read Leaderboard Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read information about a specific leaderboard.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Read Game Center Leaderboard Information`](./get-v2-gamecenterleaderboards-_id_.md) instead.

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829
```

**Response**:

```json
{
  “data” : {
    “type” : “gameCenterLeaderboards”,
    “id” : “843189c3-61a6-480a-a9d2-760a41299829”,
    “attributes” : {
      “defaultFormatter” : “INTEGER”,
      “referenceName” : “Latte Art”,
      “vendorIdentifier” : “LA_LB”,
      “submissionType” : “BEST_SCORE”,
      “scoreSortType” : “DESC”,
      “scoreRangeStart” : “1”,
      “scoreRangeEnd” : “100”,
      “recurrenceStartDate” : “2023-09-02T07:00:00Z”,
      “recurrenceDuration” : “PT168H”,
      “recurrenceRule” : “FREQ=DAILY;INTERVAL=7”,
      “archived” : false
    },
    “relationships” : {
      “groupLeaderboard” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/relationships/groupLeaderboard”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/groupLeaderboard”
        }
      },
      “localizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/relationships/localizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/localizations”
        }
      },
      “releases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/relationships/releases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/releases”
        }
      },
      “leaderboardScores” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/relationships/leaderboardScores”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/leaderboardScores”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the leaderboard resource ID from the [`Get leaderboards information`](./get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md) response.

### Query Parameters

- `fields[gameCenterLeaderboardLocalizations]` ([string]) *(deprecated)*: **Allowed Values**: `locale`, `name`, `formatterOverride`, `formatterSuffix`, `formatterSuffixSingular`, `description`, `gameCenterLeaderboard`, `gameCenterLeaderboardImage`
- `fields[gameCenterLeaderboardReleases]` ([string]) *(deprecated)*: **Allowed Values**: `live`, `gameCenterDetail`, `gameCenterLeaderboard`
- `fields[gameCenterLeaderboards]` ([string]): **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`
- `include` ([string]): **Allowed Values**: `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`
- `limit[gameCenterLeaderboardSets]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[localizations]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[releases]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[gameCenterActivities]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `playStyle`, `minimumPlayersCount`, `maximumPlayersCount`, `supportsPartyCode`, `archived`, `properties`, `gameCenterDetail`, `gameCenterGroup`, `achievements`, `achievementsV2`, `leaderboards`, `leaderboardsV2`, `versions`
- `fields[gameCenterChallenges]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `archived`, `challengeType`, `repeatable`, `gameCenterDetail`, `gameCenterGroup`, `versions`, `leaderboard`, `leaderboardV2`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[gameCenterGroups]` ([string]): **Allowed Values**: `referenceName`, `gameCenterDetails`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`
- `fields[gameCenterLeaderboardSets]` ([string]) *(deprecated)*: **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`

## Responses

- `200` OK (`GameCenterLeaderboardResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading leaderboards
- [Read Game Center Leaderboard Information](./get-v2-gamecenterleaderboards-_id_.md)
  Get information about a specific Game Center leaderboard.
- [List All Versions for a Game Center Leaderboard](./get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Get All Version IDs for a Game Center Leaderboard](./get-v2-gamecenterleaderboards-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard.
- [Read Group Information for a Leaderboard](./get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List All Localizations for a Leaderboard](./get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [List localization IDs for a Game Center leaderboard](./get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List all groups to which a leaderboard belongs](./get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List Releases for a Leaderboard](./get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [List release IDs for a Game Center leaderboard](./get-v1-gamecenterleaderboards-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboards-_id_)*