# alias

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A string the player chooses to identify themself to other players.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var alias: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nonnull) NSString * alias;
```

*macOS*

```objc
@property (atomic, copy, readonly, nonnull) NSString * alias;
```

## Discussion

GameKit uses the player’s alias when a player isn’t a friend of the local player. Typically, you never display the alias string directly in your user interface. Instead use the [`displayName`](./displayname.md) property.

## See Also

### Accessing player details
- [var displayName: String](./displayname.md)
  A string to display for the player.
- [var isInvitable: Bool](./isinvitable.md)
  A Boolean value that indicates whether the local player can send an invitation to the player.
- [var isFriend: Bool](./isfriend.md)
  A Boolean value that indicates whether the player is a friend of the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/alias)*