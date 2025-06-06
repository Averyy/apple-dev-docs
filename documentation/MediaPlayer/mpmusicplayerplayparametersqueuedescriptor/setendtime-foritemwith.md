# setEndTime(_:forItemWith:)

**Framework**: Media Player  
**Kind**: method

Sets the time the item with the associated play parameters is to stop playing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setEndTime(_ endTime: TimeInterval, forItemWith playParameters: MPMusicPlayerPlayParameters)
```

## Parameters

- `endTime`: The   describing when the item with designated play parameters stops playing.
- `playParameters`: The play parameters associated with the item in the queue that has a changed end time.

## See Also

- [func setStartTime(TimeInterval, forItemWith: MPMusicPlayerPlayParameters)](mpmusicplayerplayparametersqueuedescriptor/setstarttime(_:foritemwith:).md)
  Sets the time the item with the associated play parameters is to start playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/setendtime(_:foritemwith:))*