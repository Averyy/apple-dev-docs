# Delete a Leaderboard Set Release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a new leaderboard set release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetReleases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set releases
- [Read Leaderboard Set Release Information](./get-v1-gamecenterleaderboardsetreleases-_id_.md)
  Get information about a leaderboard set release.
- [Create a Leaderboard Set Release](./post-v1-gamecenterleaderboardsetreleases.md)
  Add a new leaderboard set release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterleaderboardsetreleases-_id_)*