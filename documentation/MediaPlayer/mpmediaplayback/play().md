# play()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Initiates playback of the current item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func play()
```

```objc
- (void) play;
```

## Mentions

- [Playing audio using the built-in music player](../playing-audio-using-the-built-in-music-player.md)

## Discussion

If playback was previously paused, this method resumes playback where it left off; otherwise, this method plays the first available item, from the beginning.

If a media player isn’t prepared for playback when you call this method, this method first prepares the media player and then starts playback. To minimize playback delay, call the [`prepareToPlay()`](./preparetoplay%28%29.md) method before you call this method.

To receive a notification when a movie player is ready to play, register for the [`MPMoviePlayerLoadStateDidChangeNotification`](../mpmovieplayerloadstatedidchangenotification.md) notification. You can then check load state by accessing the movie player’s [`loadState`](../mpmovieplayercontroller/loadstate.md) property.

## See Also

### Starting and stopping playback
- [func pause()](./pause%28%29.md)
  Pauses playback of the current item.
- [func stop()](./stop%28%29.md)
  Ends playback of the current item.
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares a media player for playback.
- [var isPreparedToPlay: Bool](./ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/play())*