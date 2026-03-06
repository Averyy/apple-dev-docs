# GameCenterMatchmakingTestRequestInlineCreate.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes for a sample match request.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingTestRequestInlineCreate.Attributes
```

## Properties

- `appVersion` (string) *(required)*: The app version of the game that makes the request.
- `bundleId` (string) *(required)*: The bundle ID of the game that makes the request.
- `locale` (string): The language and region that the player who initiates this match request uses. The default value is `EN-US`.
- `location` (Location): The physical location where this request originates. The default value is `0, 0`.
- `maxPlayers` (integer): The maximum number of players that can join the match. This is the same value as the `GKMatchRequest.`[`maxPlayers`](https://developer.apple.com/documentation/GameKit/GKMatchRequest/maxPlayers) property that you set when submitting a request from a native app. The default value is `16`.
- `minPlayers` (integer): The minimum number of players that can join the match. This is the same value as the `GKMatchRequest.`[`minPlayers`](https://developer.apple.com/documentation/GameKit/GKMatchRequest/minPlayers) property that you set when submitting a request from a native app. The default value is `2`.
- `platform` (Platform) *(required)*: The platform of the game that makes the request.
- `playerCount` (integer): The total number of players invited to join the match including the player who initiates the match request.
- `requestName` (string) *(required)*: A unique identifier for the request.
- `secondsInQueue` (integer) *(required)*: The age of the request in seconds.

## See Also

- [object GameCenterMatchmakingTestRequestInlineCreate.Relationships](gamecentermatchmakingtestrequestinlinecreate/relationships-data.dictionary.md)
  The relationships of a match request to other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingtestrequestinlinecreate/attributes-data.dictionary)*