# setStartTime(_:forItemWith:)

**Framework**: Media Player  
**Kind**: method

Sets the time the item with the associated play parameters is to start playing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setStartTime(_ startTime: TimeInterval, forItemWith playParameters: MPMusicPlayerPlayParameters)
```

## Parameters

- `startTime`: The   describing when the item with designated play parameters starts playing.
- `playParameters`: The play parameters associated with the item in the queue that has a changed start time.

## See Also

- [func setEndTime(TimeInterval, forItemWith: MPMusicPlayerPlayParameters)](mpmusicplayerplayparametersqueuedescriptor/setendtime(_:foritemwith:).md)
  Sets the time the item with the associated play parameters is to stop playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/setstarttime(_:foritemwith:))*