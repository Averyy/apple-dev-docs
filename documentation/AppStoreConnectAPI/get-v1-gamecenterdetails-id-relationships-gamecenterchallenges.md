# Read challenge ids for a game center detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all the challenge IDs for a specific Game Center detail.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterChallenges`

## Parameters

- `limit` (integer)

## See Also

- [Read the state of game center for an app](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [Read game center details](get-v1-gamecenterdetails-_id_.md)
  Read a specific Game Center detail and related information.
- [Read app versions for a game center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [List Game Center app version IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [Read the groups in a game center detail](get-v1-gamecenterdetails-_id_-gamecentergroup.md)
  Get a list of groups in a Game Center detail.
- [Get the Game Center group ID for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-gamecentergroup.md)
- [Read the challenges for a game center detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-relationships-gamecenterchallenges)*