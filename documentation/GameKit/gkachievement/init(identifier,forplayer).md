# init(identifier:forPlayer:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Initializes an achievement for a specific player.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
init?(identifier: String?, forPlayer playerID: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier forPlayer:(NSString *) playerID;
```

#### Discussion

Your game initializes a new achievement object for a specific player only when it has not previously reported progress for that achievement. Use this method to submit a participant’s achievement when ending a turn-based match.

## Parameters

- `identifier`: A string that matches the identifier string for an achievement you created for your game in App Store Connect.
- `playerID`: The identifier for the player associated with the specified achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/init(identifier:forplayer:))*