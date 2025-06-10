# init(player:templateItem:timeRange:)

**Framework**: AVFoundation  
**Kind**: init

Creates a player looper that continuously plays the specified time range of a player item.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(player: AVQueuePlayer, templateItem itemToLoop: AVPlayerItem, timeRange loopRange: CMTimeRange)
```

#### Return Value

An new instance of `AVPlayerLooper`.

#### Discussion

The player item you specify will be used as a  to generate at least 3 player item replicas that will be inserted into the specified player’s queue to accomplish the looping playback. As the player item will only be used as a template, and not for actual playback, any changes you make to the player item after initialization will not be reflected in the replicas. If you need to explicitly configure the replica player items, such as adding instances of [`AVPlayerItemOutput`](avplayeritemoutput.md) to them, you can access them through the [`loopingPlayerItems`](avplayerlooper/loopingplayeritems.md) property.

> ❗ **Important**:  The specified player item’s asset should have its [`duration`](avasset/duration.md) property loaded before you initialize this class so that initialization will not be blocked while waiting for the [`duration`](avasset/duration.md) to become known. An [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) will be raised if the player item has a duration of 0.

You should not modify the player’s queue while `AVPlayerLooper` is performing looping playback. If you need to perform any additional configuration of the player prior to playback, you should set its [`rate`](avplayer/rate.md) to `0.0`, perform the required configuration, and then begin playback once the configuration is complete.

The [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) you specify will limit each item’s loop iteration to playing within the specified time range. To loop the full duration of the asset, specify a time range value of [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange/invalid) for the `timeRange` parameter. Time range looping will be accomplished by seeking to the time range’s start time and setting player item’s [`forwardPlaybackEndTime`](avplayeritem/forwardplaybackendtime.md) property on the looping item replicas.

> ❗ **Important**:  An [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) will be raised if the time range you specify has a duration of 0 or is not contained within the time range of the template player item.

## Parameters

- `player`: The queue player to use for playback. The player must not be  .
- `itemToLoop`: The player item to loop, which must not be  .
- `loopRange`: The player item time range to loop. Passing a value of   is equivalent to a time range of [0, player item’s duration].

## See Also

- [init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange, existingItemsOrdering: AVPlayerLooper.ItemOrdering)](avplayerlooper/init(player:templateitem:timerange:existingitemsordering:).md)
  Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.
- [convenience init(player: AVQueuePlayer, templateItem: AVPlayerItem)](avplayerlooper/init(player:templateitem:).md)
  Creates a player looper that continuously plays the full duration of a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/init(player:templateitem:timerange:))*