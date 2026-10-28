# playerWithPlayerItem:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new player initialized to play the specified player item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) playerWithPlayerItem:(AVPlayerItem *) item;
```

## Return Value

A new player initialized to play `item`.

## Parameters

- `item`: The player item to play.

## See Also

### Creating a player
- [+ playerWithURL:](./playerwithurl_.md)
  Returns a new player to play a single audiovisual resource referenced by a given URL.
- [init(url: URL)](./init%28url%29-87cxx.md)
  Creates a new player to play a single audiovisual resource referenced by a given URL.
- [init(playerItem: AVPlayerItem?)](./init%28playeritem%29.md)
  Creates a new player to play the specified player item.
- [init()](./init%28%29.md)
  Creates a player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/playerwithplayeritem:)*