# playerProperties

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The properties for other players that matchmaking rules uses to find players, with some additions.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+

## Declaration

```swift
var playerProperties: [GKPlayer : [String : Any]]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<GKPlayer *,NSDictionary<NSString *,id> *> * playerProperties;
```

#### Discussion

This property is similar to the [`GKMatchRequest`](../gkmatchrequest.md).[`recipientProperties`](../gkmatchrequest/recipientproperties.md) property but with some additions that Game Center may add. For example, if you add team rules to your rule set, use the `gc` and `team` keys to get the name of the player’s team, similar to [`properties`](./properties.md).

## See Also

### Matchmaking using rules
- [var properties: [String : Any]?](./properties.md)
  The local player’s properties that matchmaking rules uses to find the players, with some additions.
- [GKMatchProperties](../gkmatchproperties.md)
  A type for game-specific properties that Game Center uses to find players when using matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchedplayers/playerproperties)*