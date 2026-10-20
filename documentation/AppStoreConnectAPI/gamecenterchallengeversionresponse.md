# GameCenterChallengeVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single version of a Game Center challenge.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object GameCenterChallengeVersionResponse
```

## Properties

- `data` (GameCenterChallengeVersion) *(required)*
- `included` ([*]): **Allowed Types**: `GameCenterChallengeImage`, `GameCenterChallengeLocalization`, `GameCenterChallengeVersionRelease`, `GameCenterChallenge`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object GameCenterChallengeVersion](./gamecenterchallengeversion.md)
  The data structure that represent a challenge version.
- [object GameCenterChallengeVersionCreateRequest](./gamecenterchallengeversioncreaterequest.md)
  The request body you use to create a challenge version.
- [object GameCenterChallengeVersionsResponse](./gamecenterchallengeversionsresponse.md)
  A response that contains multiple challenge version  resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterchallengeversionresponse)*