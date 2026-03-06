# Create a leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a new leaderboard to your app.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)
- [Configuring Game center activities](configuring-game-center-activities.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST  https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards-d 
{
    “data”: {
        “type”: “gameCenterLeaderboards”,
        “attributes”: {
            “referenceName”: “Cortado Temp LB”,
            “vendorIdentifier”: “CORTADOTEMP_LB”,
            “defaultFormatter”: “INTEGER”,
            “submissionType”: “BEST_SCORE”,
            “scoreSortType”: “DESC”,
            “scoreRangeStart”: “0”,
            “scoreRangeEnd”: “100”
        },
        “relationships”: {
            “gameCenterDetail”: {
                “data”: {
                    “type”: “gameCenterDetails”,
                    “id”: “6fd13854-b796-4cb5-87e1-9f2d15d3d7b9”
                }
            }
        }
    }
}
```

**Response**:

```json
{
  “data” : {
    “type” : “gameCenterLeaderboards”,
    “id” : “8e76c29a-4d4d-4b1f-9389-0dd161cab83c”,
    “attributes” : {
      “defaultFormatter” : “INTEGER”,
      “referenceName” : “Cortado Temp LB”,
      “vendorIdentifier” : “CORTADOTEMP_LB”,
      “submissionType” : “BEST_SCORE”,
      “scoreSortType” : “DESC”,
      “scoreRangeStart” : “0”,
      “scoreRangeEnd” : “100”,
      “recurrenceStartDate” : null,
      “recurrenceDuration” : null,
      “recurrenceRule” : null,
      “archived” : false,
      “leaderboardType” : “CLASSIC”
    },
    “relationships” : {
      “groupLeaderboard” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/relationships/groupLeaderboard”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/groupLeaderboard”
        }
      },
      “localizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/relationships/localizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/localizations”
        }
      },
      “releases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/relationships/releases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/releases”
        }
      },
      “leaderboardScores” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/relationships/leaderboardScores”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c/leaderboardScores”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/8e76c29a-4d4d-4b1f-9389-0dd161cab83c”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards”
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards`

## See Also

- [Create a Game Center leaderboard](post-v2-gamecenterleaderboards.md)
  Create a Game Center leaderboard.
- [Modify a Game Center leaderboard](patch-v2-gamecenterleaderboards-_id_.md)
  Update a specific Game Center leaderboard.
- [Modify the activity for a Game Center leaderboard](patch-v2-gamecenterleaderboards-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center leaderboard.
- [Modify the challenge for a Game Center leaderboard](patch-v2-gamecenterleaderboards-_id_-relationships-challenge.md)
  Update the challenge relationship for a specific Game Center leaderboard.
- [Delete a Game Center leaderboard](delete-v2-gamecenterleaderboards-_id_.md)
  Delete a specific Game Center leaderboard.
- [Edit a leaderboard](patch-v1-gamecenterleaderboards-_id_.md)
  Modify the details of a leaderboard.
- [Edit the relationship between a leaderboard and a group leaderboard](patch-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  Modify the group leadboard to which a leaderboard belongs.
- [PATCH /v1/gameCenterLeaderboards/{id}/relationships/activity](patch-v1-gamecenterleaderboards-_id_-relationships-activity.md)
- [PATCH /v1/gameCenterLeaderboards/{id}/relationships/challenge](patch-v1-gamecenterleaderboards-_id_-relationships-challenge.md)
- [Delete a leaderboard](delete-v1-gamecenterleaderboards-_id_.md)
  Delete a leaderboard from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterleaderboards)*