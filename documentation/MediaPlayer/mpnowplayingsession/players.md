# players

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The array of players associated with the session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var players: [AVPlayer] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<AVPlayer *> * players;
```

## See Also

### Managing players
- [func addPlayer(AVPlayer)](./addplayer%28_%29.md)
  Adds a player to the session.
- [func removePlayer(AVPlayer)](./removeplayer%28_%29.md)
  Removes a player from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/players)*