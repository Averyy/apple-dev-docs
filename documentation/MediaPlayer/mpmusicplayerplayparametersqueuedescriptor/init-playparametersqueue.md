# init(playParametersQueue:)

**Framework**: Media Player  
**Kind**: init

Creates a new queue descriptor using the designated queue of play parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(playParametersQueue: [MPMusicPlayerPlayParameters])
```

#### Return Value

A new queue descriptor consisting of the items described by the play parameters.

## Parameters

- `playParametersQueue`: An array of play parameters created from the JSON information returned from a MusicKit query and used to populate the queue descriptor.

## See Also

- [class MPMusicPlayerPlayParameters](mpmusicplayerplayparameters.md)
  The MusicKit parameters that describe items to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/init(playparametersqueue:))*