# setEndTime(_:forItemWith:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setEndTime:(NSTimeInterval) endTime forItemWithPlayParameters:(MPMusicPlayerPlayParameters *) playParameters;
```

## Parameters

- `endTime`: The [`TimeInterval`](../../Foundation/timeinterval.md) describing when the item with designated play parameters stops playing.
- `playParameters`: The play parameters associated with the item in the queue that has a changed end time.

## See Also

### Setting start and end times
- [func setStartTime(TimeInterval, forItemWith: MPMusicPlayerPlayParameters)](./setstarttime%28_,foritemwith%29.md)
  Sets the time the item with the associated play parameters is to start playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/setendtime(_:foritemwith:))*