# Add a Player's Score

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a new entry for a player’s score for a Game Center achievement.

**Availability**:
- App Store Connect API 3.2+

## Mentions

- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)
- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)

#### Discussion

Use the `preReleased` attribute to indicate whether the requested change applies to the game’s release version or its prerelease version. Set `preReleased` to `true` to indicate that the change applies to the game’s prerelease version.

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
      “vendorIdentifier”: “com.apple.sample.actionship.perfectaim”,
      "preReleased": true
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
      “vendorIdentifier”: “com.apple.sample.actionship.perfectaim”,
      "preReleased": true
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