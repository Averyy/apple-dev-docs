# Modify a Game Center Score Moderation

**Framework**: App Store Connect API  
**Kind**: httpRequest

Block or unblock a score submitted to a leaderboard.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](app-store-connect-api-4-5-release-notes.md)

#### Overview

Blocking a score removes it from the leaderboard, and unblocking reinstates it. The response contains the updated [`GameCenterScoreModeration`](gamecenterscoremoderation.md) in a [`GameCenterScoreModerationResponse`](gamecenterscoremoderationresponse.md).

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterScoreModerations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the score moderation resource ID from the [`List Score Moderations for a Leaderboard`](get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md) response.

## Request Body

The request body you use to modify a Game Center score moderation. See [`GameCenterScoreModerationUpdateRequest`](gamecenterscoremoderationupdaterequest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterscoremoderations-_id_)*