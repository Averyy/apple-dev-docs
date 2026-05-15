# Read Leaderboard Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read information about a specific leaderboard.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `fields[gameCenterLeaderboardReleases]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `include` ([string])
- `limit[gameCenterLeaderboardSets]` (integer)
- `limit[localizations]` (integer)
- `limit[releases]` (integer)
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterChallenges]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])

## See Also

- [Read Game Center Leaderboard Information](get-v2-gamecenterleaderboards-_id_.md)
  Get information about a specific Game Center leaderboard.
- [List All Versions for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Get All Version IDs for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard.
- [Read Group Information for a Leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List All Localizations for a Leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/localizations](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List All Groups to Which a Leaderboard Belongs](get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List Releases for a Leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/releases](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboards-_id_)*