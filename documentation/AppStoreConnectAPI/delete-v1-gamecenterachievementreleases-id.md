# Delete a game center achievement release

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a release of an achievement or Game Center detail.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievementReleases/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center achievement release resource ID from the [`List achievement releases`](get-v1-gamecenterdetails-_id_-achievementreleases.md) response.

## See Also

- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [Read Release Information for an Achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [Read game center achievement release information](get-v1-gamecenterachievementreleases-_id_.md)
  Read the state of a specific achievement release.
- [Create a game center achievement release](post-v1-gamecenterachievementreleases.md)
  Create a release for an achievement and a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterachievementreleases-_id_)*