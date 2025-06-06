# init(url:)

**Framework**: AVFoundation  
**Kind**: init

Creates a new player to play a single audiovisual resource referenced by a given URL.

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
init(url URL: URL)
```

#### Return Value

A new player instance initialized to play the audiovisual resource specified by `URL`.

#### Discussion

This method implicitly creates an [`AVPlayerItem`](avplayeritem.md) object. You can get the player item using [`currentItem`](avplayer/currentitem.md).

## Parameters

- `URL`: A URL that identifies an audiovisual resource.

## See Also

- [init(playerItem: AVPlayerItem?)](avplayer/init(playeritem:).md)
  Creates a new player to play the specified player item.
- [init()](avplayer/init.md)
  Creates a player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/init(url:))*