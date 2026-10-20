# setEndTime(_:for:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

The time the designated media item is to stop playing.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setEndTime(_ endTime: TimeInterval, for mediaItem: MPMediaItem)
```

```objc
- (void) setEndTime:(NSTimeInterval) endTime forItem:(MPMediaItem *) mediaItem;
```

## Parameters

- `endTime`: The [`TimeInterval`](../../Foundation/timeinterval.md) describing when the media item stops playing.
- `mediaItem`: The media item in the queue that has a changed end time.

## See Also

### Setting start and end times
- [func setStartTime(TimeInterval, for: MPMediaItem)](./setstarttime%28_,for%29.md)
  The time the designated media item is to start playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/setendtime(_:for:))*