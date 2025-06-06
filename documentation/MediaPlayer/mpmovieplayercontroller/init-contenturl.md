# init(contentURL:)

**Framework**: Media Player  
**Kind**: init

Returns a `MPMoviePlayerController` object initialized with the movie at the specified URL.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
init!(contentURL url: URL!)
```

#### Return Value

The movie player object.

#### Discussion

This method initializes a movie player, but does not prepare it for playback. To prepare a new movie player for playback, call the [`prepareToPlay()`](mpmediaplayback/preparetoplay().md) method, described in [`MPMediaPlayback`](mpmediaplayback.md).

To be notified when a new movie player is ready to play, register for the [`MPMoviePlayerLoadStateDidChangeNotification`](mpmovieplayerloadstatedidchangenotification.md) notification. You can then check load state by accessing the [`loadState`](mpmovieplayercontroller/loadstate.md) property.

To check for errors in URL loading, register for the [`MPMoviePlayerPlaybackDidFinishNotification`](mpmovieplayerplaybackdidfinishnotification.md) notification. On error, this notification contains an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object available using the `@"error"` key in the notification’s `userInfo` dictionary.

## Parameters

- `url`: The location of the movie file. This file must be located either in your app directory or on a remote server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/init(contenturl:))*