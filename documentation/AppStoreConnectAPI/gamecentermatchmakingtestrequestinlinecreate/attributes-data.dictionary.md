# GameCenterMatchmakingTestRequestInlineCreate.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The attributes for a sample match request.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```
object GameCenterMatchmakingTestRequestInlineCreate.Attributes
```

## Properties

- `appVersion` (string): The app version of the game that makes the request.
- `bundleId` (string): The bundle ID of the game that makes the request.
- `locale` (string): The language and region that the player who initiates this match request uses. The default value is `EN-US`.

  **Allowed Values**: `AR-SA`, `CA-ES`, `CS-CZ`, `DA-DK`, `DE-DE`, `EL-GR`, `EN-AU`, `EN-GB`, `EN-US`, `EN-KY`, `ES-ES`, `ES-MX`, `FI-FI`, `FR-CA`, `FR-FR`, `HI-IN`, `HR-HR`, `HU-HU`, `ID-ID`, `IT-IT`, `IW-IL`, `JA-JP`, `KO-KR`, `MS-MY`, `NL-NL`, `NO-NO`, `PL-PL`, `PT-BR`, `PT-PT`, `RO-RO`, `RU-RU`, `SK-SK`, `SV-SE`, `TH-TH`, `TR-TR`, `UK-UA`, `ZH-CN`, `ZH-TW`, `ZH-HK`
- `location` (Location): The physical location where this request originates. The default value is `0, 0`.
- `maxPlayers` (integer): The maximum number of players that can join the match. This is the same value as the `GKMatchRequest.`[`maxPlayers`](../../GameKit/gkmatchrequest/maxplayers.md) property that you set when submitting a request from a native app. The default value is `16`.
- `minPlayers` (integer): The minimum number of players that can join the match. This is the same value as the `GKMatchRequest.`[`minPlayers`](../../GameKit/gkmatchrequest/minplayers.md) property that you set when submitting a request from a native app. The default value is `2`.
- `platform` (Platform): The platform of the game that makes the request.
- `playerCount` (integer): The total number of players invited to join the match including the player who initiates the match request.
- `requestName` (string): A unique identifier for the request.
- `secondsInQueue` (integer): The age of the request in seconds.

## See Also

### Objects
- [object GameCenterMatchmakingTestRequestInlineCreate.Relationships](./relationships-data.dictionary.md)
  The relationships of a match request to other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingtestrequestinlinecreate/attributes-data.dictionary)*