# Read Achievement Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read information about a specific Game Center achievement.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterAchievements
```

**Response**:

```json
{
  “data” : [ {
    “type” : “gameCenterAchievements”,
    “id” : “d3888910-d5fd-4737-b903-2f54356ce682”,
    “attributes” : {
      “referenceName” : “Ristretto”,
      “vendorIdentifier” : “RISTRETTO_ACH”,
      “points” : 0,
      “showBeforeEarned” : false,
      “repeatable” : false,
      “archived” : false
    },
    “relationships” : {
      “groupAchievement” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682/relationships/groupAchievement”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682/groupAchievement”
        }
      },
      “localizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682/relationships/localizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682/localizations”
        }
      },
      “releases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682/relationships/releases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682/releases”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/d3888910-d5fd-4737-b903-2f54356ce682”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterDetails/6fd13854-b796-4cb5-87e1-9f2d15d3d7b9/gameCenterAchievements”
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

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}`

## Parameters

- `fields[gameCenterAchievementLocalizations]` ([string])
- `fields[gameCenterAchievementReleases]` ([string])
- `fields[gameCenterAchievements]` ([string])
- `include` ([string])
- `limit[localizations]` (integer)
- `limit[releases]` (integer)
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])

## See Also

- [Read Game Center Achievement Information](get-v2-gamecenterachievements-_id_.md)
  Get information about a specific Game Center achievement.
- [List All Versions for a Game Center Achievement](get-v2-gamecenterachievements-_id_-versions.md)
  Get a list of versions for a specific Game Center achievement.
- [Get All Version IDs for a Game Center Achievement](get-v2-gamecenterachievements-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center achievement.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [List All Localizations for an Achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [Read Release Information for an Achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [List Associated Group Achievement Information for an Achievement](get-v1-gamecenterachievements-_id_-groupachievement.md)
  Read information about the group for specific achievement.
- [List Group Achievements for an Achievement](get-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  List associated group achievements for a specific achievement.
- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievements-_id_)*