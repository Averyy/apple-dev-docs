# Modify an achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify properties for a specific achievement.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502 -d {
  “data”: {
    “type”: “gameCenterAchievements”,
    “id”: “304e0f56-63b2-492f-980e-bce6fafb8502”,
    “attributes”: {
      “repeatable”: true
    }
  }
}

```

**Response**:

```json

  “data” : {
    “type” : “gameCenterAchievements”,
    “id” : “304e0f56-63b2-492f-980e-bce6fafb8502”,
    “attributes” : {
      “referenceName” : “Perfectly Steamed Milk Texture”,
      “vendorIdentifier” : “PSMT_ACH”,
      “points” : 0,
      “showBeforeEarned” : false,
      “repeatable” : true,
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
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502”
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List all achievements`](get-v1-gamecenterdetails-_id_-gamecenterachievements.md) response.

## See Also

- [Create a Game Center achievement](post-v2-gamecenterachievements.md)
  Create a Game Center achievement.
- [Modify a Game Center achievement](patch-v2-gamecenterachievements-_id_.md)
  Update a specific Game Center achievement.
- [Modify the activity for a Game Center achievement](patch-v2-gamecenterachievements-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center achievement.
- [Delete a Game Center achievement](delete-v2-gamecenterachievements-_id_.md)
  Delete a specific Game Center achievement.
- [Create an achievement](post-v1-gamecenterachievements.md)
  Add an achievement to a Game Center detail.
- [Modify the group for an achievement](patch-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  Modify the achievement group for a specific achievement.
- [PATCH /v1/gameCenterAchievements/{id}/relationships/activity](patch-v1-gamecenterachievements-_id_-relationships-activity.md)
- [Delete an achievement](delete-v1-gamecenterachievements-_id_.md)
  Delete a specific achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterachievements-_id_)*