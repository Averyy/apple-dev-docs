# init(player:templateItem:)

**Framework**: AVFoundation  
**Kind**: init

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

#### Return Value

An new instance of `AVPlayerLooper`.

#### Discussion

Creating an instance of this class using this method is equivalent to calling [`init(player:templateItem:timeRange:)`](avplayerlooper/init(player:templateitem:timerange:).md) and passing a value of [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange/invalid) for the `timeRange` parameter.

## Parameters

- `player`: The queue player to use for playback. The player must not be  .
- `itemToLoop`: The player item to loop, which must not be  .

## See Also

- [init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange, existingItemsOrdering: AVPlayerLooper.ItemOrdering)](avplayerlooper/init(player:templateitem:timerange:existingitemsordering:).md)
  Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.
- [convenience init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange)](avplayerlooper/init(player:templateitem:timerange:).md)
  Creates a player looper that continuously plays the specified time range of a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/init(player:templateitem:))*