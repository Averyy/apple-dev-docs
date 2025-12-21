# loopingPlayerItems

**Framework**: AVFoundation  
**Kind**: property

An array containing replicas of the template player item used to accomplish the looping.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var loopingPlayerItems: [AVPlayerItem] { get }
```

#### Discussion

`AVPlayerLooper` creates replicas of the template [`AVPlayerItem`](avplayeritem.md) using the [`copyWithZone:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/copyWithZone:) method and inserts them in the queue player’s queue to accomplish the looping. You can determine the number of replicas created and can listen for notifications and property changes from the replicas if desired.

Access to the [`AVPlayerItem`](avplayeritem.md) replicas are for informational purposes and to allow you to apply any configuration that is not transferred from the template player item to the replicas. For instance, any instances of [`AVPlayerItemOutput`](avplayeritemoutput.md) and [`AVPlayerItemMediaDataCollector`](avplayeritemmediadatacollector.md) attached to the template player item are not transferred to the replicas so you should add them to each replica item if needed.

> ❗ **Important**:  You should not modify any properties of the replicas that would disrupt looping playback. This includes properties such as the playhead time/date, selected media option, and forward playback end time.

## See Also

- [func disableLooping()](avplayerlooper/disablelooping.md)
  Disables looping for the player queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/loopingplayeritems)*