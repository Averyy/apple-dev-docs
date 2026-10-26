# init(playerItem:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a new player to play the specified player item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
init(playerItem item: AVPlayerItem?)
```

```objc
- (instancetype) initWithPlayerItem:(AVPlayerItem *) item;
```

#### Return Value

A new player initialized to play `item`.

## Parameters

- `item`: The player item to play.

## See Also

### Creating a player
- [init(url: URL)](./init%28url%29-87cxx.md)
  Creates a new player to play a single audiovisual resource referenced by a given URL.
- [init()](./init%28%29.md)
  Creates a player object.
- [+ playerWithURL:](./playerwithurl_.md)
  Returns a new player to play a single audiovisual resource referenced by a given URL.
- [+ playerWithPlayerItem:](./playerwithplayeritem_.md)
  Returns a new player initialized to play the specified player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/init(playeritem:))*