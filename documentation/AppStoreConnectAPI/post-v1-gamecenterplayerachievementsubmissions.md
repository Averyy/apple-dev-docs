# POST /v1/gameCenterPlayerAchievementSubmissions

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a new entry for a player’s score for a Game Center achievement.

**Availability**:
- App Store Connect API 3.2+

## Mentions

- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/gameCenterPlayerAchievementSubmissions
{
  “data”: {
    “type”: “gameCenterPlayerAchievementSubmissions”,
    “attributes”: {
      “percentageAchieved”: 30,
      “scopedPlayerId”: “A:_5f21e308073d18f9b3afdc37f646e851”,
      “bundleId”: “com.apple.sample.actionship”,
      “vendorIdentifier”: “com.apple.sample.actionship.perfectaim”
    }
  }
}

```

**Response**:

```json
{
  “data”: {
    “type”: “gameCenterPlayerAchievementSubmissions”,
    “id”: “d9f8b8dd-6050-45c6-a8e3-c6b97c186583”,
    “attributes”: {
      “bundleId”: “com.apple.sample.actionship”,
      “challengeIds”: null,
      “percentageAchieved”: 30,
      “scopedPlayerId”: “A:_5f21e308073d18f9b3afdc37f646e851”,
      “submittedDate”: null,
      “vendorIdentifier”: “com.apple.sample.actionship.perfectaim”
    },
    “links”: {
      “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterPlayerAchievementSubmissions/d9f8b8dd-6050-45c6-a8e3-c6b97c186583”
    }
  },
  “links”: {
    “self”: “https://api.appstoreconnect.apple.com/v1/gameCenterPlayerAchievementSubmissions”
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterPlayerAchievementSubmissions`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterplayerachievementsubmissions)*