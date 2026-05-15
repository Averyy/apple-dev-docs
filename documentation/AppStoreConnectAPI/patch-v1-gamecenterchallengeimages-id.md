# Commit an Image for a Challenge

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an uploaded image asset as a Game Center challenge image.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game Center challenges](configuring-game-center-challenges.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterChallengeImages/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read Image Information for a Challenge Localization](get-v1-gamecenterchallengelocalizations-_id_-image.md)
  Get details about the image for a specific Game Center challenge localization.
- [Read Challenge Image Information](get-v1-gamecenterchallengeimages-_id_.md)
  Get information for a specific Game Center challenge image.
- [Create a Challenge Image](post-v1-gamecenterchallengeimages.md)
  Reserve an image for a Game Center challenge.
- [Delete a Challenge Image](delete-v1-gamecenterchallengeimages-_id_.md)
  Remove a specific image from a Game Center challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterchallengeimages-_id_)*