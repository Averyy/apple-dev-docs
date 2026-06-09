# Read Release Information for an Achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the state of an achievement release and related information.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/4a6bcd3d-0325-418b-3bbf-671bd15be8c6/releases
```

**Response**:

```json
{
  “data” : [ {
    “type” : “gameCenterAchievementReleases”,
    “id” : “be3bd01f-fd78-9093-63a7-bc25ff890eb2”,
    “attributes” : {
      “live” : true
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/be3bd01f-fd78-9093-63a7-bc25ff890eb2”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/4a6bcd3d-0325-418b-3bbf-671bd15be8c6/releases”
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

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}/releases`

## Parameters

- `fields[gameCenterAchievementReleases]` ([string])
- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterDetails]` ([string])
- `filter[gameCenterDetail]` ([string])
- `filter[live]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [Read game center achievement release information](get-v1-gamecenterachievementreleases-_id_.md)
  Read the state of a specific achievement release.
- [Create a game center achievement release](post-v1-gamecenterachievementreleases.md)
  Create a release for an achievement and a Game Center detail.
- [Delete a game center achievement release](delete-v1-gamecenterachievementreleases-_id_.md)
  Delete a release of an achievement or Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievements-_id_-releases)*