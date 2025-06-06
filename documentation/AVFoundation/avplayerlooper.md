# AVPlayerLooper

**Framework**: AVFoundation  
**Kind**: class

An object that loops media content using a queue player.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlayerLooper
```

#### Overview

You can manually implement looping playback in your app using [`AVQueuePlayer`](avqueueplayer.md), but `AVPlayerLooper` provides a much simpler interface to loop a single [`AVPlayerItem`](avplayeritem.md). You create a player looper by passing it a reference to your [`AVQueuePlayer`](avqueueplayer.md) and a template [`AVPlayerItem`](avplayeritem.md) and the looper automatically manages the looping playback of this content (see example).

```swift
let asset = // AVAsset with its 'duration' property value loaded
let playerItem = AVPlayerItem(asset: asset)
 
// Create a new player looper with the queue player and template item
playerLooper = AVPlayerLooper(player: queuePlayer, templateItem: playerItem)
 
// Begin looping playback
queuePlayer.play()
```

## Topics

### Creating a Player Looper
- [init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange, existingItemsOrdering: AVPlayerLooper.ItemOrdering)](avplayerlooper/init(player:templateitem:timerange:existingitemsordering:).md)
  Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.
- [convenience init(player: AVQueuePlayer, templateItem: AVPlayerItem)](avplayerlooper/init(player:templateitem:).md)
  Creates a player looper that continuously plays the full duration of a player item.
- [convenience init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange)](avplayerlooper/init(player:templateitem:timerange:).md)
  Creates a player looper that continuously plays the specified time range of a player item.
### Configuring Looping
- [var loopingPlayerItems: [AVPlayerItem]](avplayerlooper/loopingplayeritems.md)
  An array containing replicas of the template player item used to accomplish the looping.
- [func disableLooping()](avplayerlooper/disablelooping.md)
  Disables looping for the player queue.
### Observing Looping State
- [var loopCount: Int](avplayerlooper/loopcount.md)
  The number of times the object played the media.
- [var status: AVPlayerLooper.Status](avplayerlooper/status-swift.property.md)
  A status that indicates the object’s ability to loop playback.
- [AVPlayerLooper.Status](avplayerlooper/status-swift.enum.md)
  Status constants that indicate whether a looper can successfully perform looping playback.
### Monitoring Errors
- [var error: (any Error)?](avplayerlooper/error.md)
  An error that describes the reason looping failed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [class AVPlayer](avplayer.md)
  An object that provides the interface to control the player’s transport behavior.
- [class AVPlayerItem](avplayeritem.md)
  An object that models the timing and presentation state of an asset during playback.
- [class AVPlayerItemTrack](avplayeritemtrack.md)
  An object that represents the presentation state of an asset track during playback.
- [class AVQueuePlayer](avqueueplayer.md)
  An object that plays a sequence of player items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper)*