# GKMatchProperties

**Framework**: GameKit  
**Kind**: typealias  
**Role**: Type Alias

A type for game-specific properties that Game Center uses to find players when using matchmaking rules.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```c
typedef NSDictionary<NSString *,id> GKMatchProperties;
```

## Discussion

For more information, see [Matchmaking rules](./matchmaking-rules.md).

## See Also

### Getting matchmaking properties
- [var properties: [String : Any]?](./gkmatch/properties.md)
  The local player’s properties that matchmaking rules used to find the players with some additions.
- [var playerProperties: [GKPlayer : [String : Any]]?](./gkmatch/playerproperties.md)
  The properties for other players that matchmaking rules uses to find players, with some additions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchproperties)*