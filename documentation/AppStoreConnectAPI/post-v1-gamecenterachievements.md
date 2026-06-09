# Create an Achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add an achievement to a Game Center detail.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/gameCenterAchievements -d {
  “data”: {
    “type”: “gameCenterAchievements”,
    “attributes”: {
      “referenceName”: “Perfectly Steamed Milk Texture”,
      “vendorIdentifier”: “PSMT_ACH”,
      “points”: 0,
      “repeatable”: false,
      “showBeforeEarned”: false
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
    “type” : “gameCenterAchievements”,
    “id” : “304e0f56-63b2-492f-980e-bce6fafb8502”,
    “attributes” : {
      “referenceName” : “Perfectly Steamed Milk Texture”,
      “vendorIdentifier” : “PSMT_ACH”,
      “points” : 0,
      “showBeforeEarned” : false,
      “repeatable” : false,
      “archived” : false
    },
    “relationships” : {
      “groupAchievement” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/relationships/groupAchievement”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/groupAchievement”
        }
      },
      “localizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/relationships/localizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/localizations”
        }
      },
      “releases” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/relationships/releases”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/releases”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements”
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterAchievements`

## See Also

- [Create a Game Center Achievement](post-v2-gamecenterachievements.md)
  Create a Game Center achievement.
- [Modify a Game Center Achievement](patch-v2-gamecenterachievements-_id_.md)
  Update a specific Game Center achievement.
- [Modify the Activity for a Game Center Achievement](patch-v2-gamecenterachievements-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center achievement.
- [Delete a Game Center Achievement](delete-v2-gamecenterachievements-_id_.md)
  Delete a specific Game Center achievement.
- [Modify an Achievement](patch-v1-gamecenterachievements-_id_.md)
  Modify properties for a specific achievement.
- [Modify the Group for an Achievement](patch-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  Modify the achievement group for a specific achievement.
- [Modify the activity for a Game Center achievement](patch-v1-gamecenterachievements-_id_-relationships-activity.md)
- [Delete an Achievement](delete-v1-gamecenterachievements-_id_.md)
  Delete a specific achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterachievements)*