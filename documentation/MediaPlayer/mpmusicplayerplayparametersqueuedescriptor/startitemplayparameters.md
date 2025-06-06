# startItemPlayParameters

**Framework**: Media Player  
**Kind**: property

The item identified by the play parameters to play first.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var startItemPlayParameters: MPMusicPlayerPlayParameters? { get set }
```

#### Discussion

When this property isn’t set, the value is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) and the first item in the queue is the first item to play.

## See Also

- [var playParametersQueue: [MPMusicPlayerPlayParameters]](mpmusicplayerplayparametersqueuedescriptor/playparametersqueue.md)
  An array containing the play parameters returned from querying MusicKit.
- [class MPMusicPlayerPlayParameters](mpmusicplayerplayparameters.md)
  The MusicKit parameters that describe items to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/startitemplayparameters)*