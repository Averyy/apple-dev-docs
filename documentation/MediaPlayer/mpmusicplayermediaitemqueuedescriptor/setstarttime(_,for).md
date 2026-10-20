# setStartTime(_:for:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

The time the designated media item is to start playing.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setStartTime(_ startTime: TimeInterval, for mediaItem: MPMediaItem)
```

```objc
- (void) setStartTime:(NSTimeInterval) startTime forItem:(MPMediaItem *) mediaItem;
```

## Parameters

- `startTime`: The [`TimeInterval`](../../Foundation/timeinterval.md) describing when the media item starts playing.
- `mediaItem`: The media item in the queue that has a changed start time.

## See Also

### Setting start and end times
- [func setEndTime(TimeInterval, for: MPMediaItem)](./setendtime%28_,for%29.md)
  The time the designated media item is to stop playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/setstarttime(_:for:))*