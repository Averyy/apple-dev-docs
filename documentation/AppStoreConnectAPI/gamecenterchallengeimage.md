# GameCenterChallengeImage

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

An image asset used to represent a Game Center challenge in the player interface.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object GameCenterChallengeImage
```

## Topics

### Dictionaries
- [object GameCenterChallengeImage.Attributes](./gamecenterchallengeimage/attributes-data.dictionary.md)
  Attributes that describe a challenge resource.

## Properties

- `attributes` (GameCenterChallengeImage.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*: **Allowed Values**: `gameCenterChallengeImages`

## See Also

### Objects
- [object GameCenterChallengeImageCreateRequest](./gamecenterchallengeimagecreaterequest.md)
  The request body for uploading an image asset for a Game Center challenge.
- [object GameCenterChallengeImageResponse](./gamecenterchallengeimageresponse.md)
  A response containing a single image asset for a Game Center challenge.
- [object GameCenterChallengeImageUpdateRequest](./gamecenterchallengeimageupdaterequest.md)
  The request body you use to update a challenge.
- [object GameCenterChallengeLocalizationImageLinkageResponse](./gamecenterchallengelocalizationimagelinkageresponse.md)
- [object GameCenterChallengeVersionDefaultImageLinkageResponse](./gamecenterchallengeversiondefaultimagelinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterchallengeimage)*