# setStartTime(_:forItemWith:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setStartTime:(NSTimeInterval) startTime forItemWithPlayParameters:(MPMusicPlayerPlayParameters *) playParameters;
```

## Parameters

- `startTime`: The [`TimeInterval`](../../Foundation/timeinterval.md) describing when the item with designated play parameters starts playing.
- `playParameters`: The play parameters associated with the item in the queue that has a changed start time.

## See Also

### Setting start and end times
- [func setEndTime(TimeInterval, forItemWith: MPMusicPlayerPlayParameters)](./setendtime%28_,foritemwith%29.md)
  Sets the time the item with the associated play parameters is to stop playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/setstarttime(_:foritemwith:))*