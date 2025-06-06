# duration

**Framework**: Media Player  
**Kind**: property

The duration of the movie, measured in seconds.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var duration: TimeInterval { get }
```

#### Discussion

If the duration of the movie is not known, the value in this property is `0.0`. If the duration is subsequently determined, this property is updated and a [`MPMovieDurationAvailableNotification`](mpmoviedurationavailablenotification.md) notification is posted.

## See Also

- [var playableDuration: TimeInterval](mpmovieplayercontroller/playableduration.md)
  The amount of currently playable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/duration)*