# Enable Game Center for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a Game Center detail for an app.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterDetails -d
{
  “data”: {
    “type”: “gameCenterDetails”,
    “attributes”: {
      “challengeEnabled”: true
    },
    “relationships”: {
      “app”: {
        “data”: {
          “type”: “apps”,
          “id”: “6449448109”
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
    “type” : “gameCenterDetails”,
    “id” : “6fd13854-b796-4cb5-87e1-9f2d15d3d7b9”,
    “attributes” : {
      “arcadeEnabled” : false,
      “challengeEnabled” : true
    },
    “relationships” : {
      “gameCenterAppVersions” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/gameCenterAppVersions”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterAppVersions”
        }
      },
      “gameCenterGroup” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/gameCenterGroup”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterGroup”
        }
      },
      “gameCenterLeaderboards” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/gameCenterLeaderboards”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterLeaderboards”
        }
      },
      “gameCenterLeaderboardSets” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/gameCenterLeaderboardSets”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterLeaderboardSets”
        }
      },
      “gameCenterAchievements” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/gameCenterAchievements”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterAchievements”
        }
      },
      “achievementReleases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/achievementReleases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/achievementReleases”
        }
      },
      “leaderboardReleases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/leaderboardReleases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/leaderboardReleases”
        }
      },
      “leaderboardSetReleases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/leaderboardSetReleases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/leaderboardSetReleases”
        }
      },
      “blockedPlayers” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/relationships/blockedPlayers”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/blockedPlayers”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails”
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterDetails`

## See Also

- [Modify a Game Center Detail for an App](patch-v1-gamecenterdetails-_id_.md)
  Edit challenge state, default leaderboards, and groups.
- [Modify the Achievements for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2.md)
  Update the achievements relationship for a specific Game Center detail.
- [Modify the Leaderboard Sets for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Update the leaderboard sets relationship for a specific Game Center detail.
- [Modify the Leaderboards for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Update the leaderboards relationship for a specific Game Center detail.
- [Modify the Associated Leaderboard Sets for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  Edit the associated leaderboard sets for a Game Center detail.
- [Modify the Associated Leaderboards for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  Edit the associated leaderboards for a Game Center detail.
- [Modify the Challenges Minimum Platform Version for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterdetails)*