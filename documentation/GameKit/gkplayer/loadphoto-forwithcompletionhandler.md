# loadPhoto(for:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads a photo of the player from Game Center.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func loadPhoto(for size: GKPlayer.PhotoSize) async throws -> UIImage
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

The size of the image that returns to your game is dependent on both the size parameter and the user interface idiom of the device your game is running on.

## Parameters

- `size`: A constant that determines the size of the photo to load.
- `completionHandler`: The block receives the following parameters:

## See Also

- [GKPlayer.PhotoSize](gkplayer/photosize.md)
  The size of a photo that Game Center loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/loadphoto(for:withcompletionhandler:))*