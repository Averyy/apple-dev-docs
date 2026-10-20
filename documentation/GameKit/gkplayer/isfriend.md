# isFriend

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player is a friend of the local player.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`loadFriendPlayers(completionHandler:)`](../gklocalplayer/loadfriendplayers%28completionhandler%29.md) instead.

## Declaration

```swift
var isFriend: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) BOOL isFriend;
```

*macOS*

```objc
@property (atomic, readonly) BOOL isFriend;
```

#### Discussion

Players use the Game Center app to declare other players as friends.

## See Also

### Accessing player details
- [var alias: String](./alias.md)
  A string the player chooses to identify themself to other players.
- [var displayName: String](./displayname.md)
  A string to display for the player.
- [var isInvitable: Bool](./isinvitable.md)
  A Boolean value that indicates whether the local player can send an invitation to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/isfriend)*