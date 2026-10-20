# GameCenterLeaderboardCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create a Game Center leaderboard.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```
object GameCenterLeaderboardCreateRequest.Data
```

## Topics

### Objects
- [object GameCenterLeaderboardCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a leaderboard resource.
- [object GameCenterLeaderboardCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.
### Data Types
- [type GameCenterLeaderboardFormatter](../gamecenterleaderboardformatter.md)
  The values you can select to describe the format of a leaderboard.

## Properties

- `attributes` (GameCenterLeaderboardCreateRequest.Data.Attributes) *(required)*
- `relationships` (GameCenterLeaderboardCreateRequest.Data.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `gameCenterLeaderboards`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardcreaterequest/data-data.dictionary)*