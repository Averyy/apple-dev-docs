# Read game center achievement release information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the state of a specific achievement release.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/b46850bc-ba02-3793-4ea7-36738b92440a
```

**Response**:

```json
{
  “data” : {
    “type” : “gameCenterAchievementReleases”,
    “id” : “b46850bc-ba02-3793-4ea7-36738b92440a”,
    “attributes” : {
      “live” : true
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/b46850bc-ba02-3793-4ea7-36738b92440a”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/b46850bc-ba02-3793-4ea7-36738b92440a”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/{id}`

## Parameters

- `fields[gameCenterAchievementReleases]` ([string])
- `include` ([string])
- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterDetails]` ([string])

## See Also

- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [Read Release Information for an Achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [Create a game center achievement release](post-v1-gamecenterachievementreleases.md)
  Create a release for an achievement and a Game Center detail.
- [Delete a game center achievement release](delete-v1-gamecenterachievementreleases-_id_.md)
  Delete a release of an achievement or Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievementreleases-_id_)*