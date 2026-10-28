# duration

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The duration of the movie, measured in seconds.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var duration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval duration;
```

## Discussion

If the duration of the movie is not known, the value in this property is `0.0`. If the duration is subsequently determined, this property is updated and a [`MPMovieDurationAvailableNotification`](../mpmoviedurationavailablenotification.md) notification is posted.

## See Also

### Accessing the movie duration
- [var playableDuration: TimeInterval](./playableduration.md)
  The amount of currently playable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/duration)*