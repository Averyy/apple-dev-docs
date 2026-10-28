# init(player:templateItem:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a player looper that continuously plays the full duration of a player item.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(player: AVQueuePlayer, templateItem itemToLoop: AVPlayerItem)
```

```objc
+ (instancetype) playerLooperWithPlayer:(AVQueuePlayer *) player templateItem:(AVPlayerItem *) itemToLoop;
```

## Return Value

An new instance of `AVPlayerLooper`.

## Discussion

Creating an instance of this class using this method is equivalent to calling [`init(player:templateItem:timeRange:)`](./init%28player,templateitem,timerange%29.md) and passing a value of [`invalid`](../../CoreMedia/cmtimerange/invalid.md) for the `timeRange` parameter.

## Parameters

- `player`: The queue player to use for playback. The player must not be `nil`.
- `itemToLoop`: The player item to loop, which must not be `nil`.

## See Also

### Creating a player looper
- [init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange, existingItemsOrdering: AVPlayerLooper.ItemOrdering)](./init%28player,templateitem,timerange,existingitemsordering%29.md)
  Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.
- [convenience init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange)](./init%28player,templateitem,timerange%29.md)
  Creates a player looper that continuously plays the specified time range of a player item.
- [+ playerLooperWithPlayer:templateItem:timeRange:](./playerlooperwithplayer_templateitem_timerange_.md)
  Returns player looper that continuously plays the specified time range of a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/init(player:templateitem:))*