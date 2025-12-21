# AVQueuePlayer

**Framework**: AVFoundation  
**Kind**: class

An object that plays a sequence of player items.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@MainActor
class AVQueuePlayer
```

## Mentions

- [Implementing simple enhanced buffering for your content](implementing-simple-enhanced-buffering-for-your-content.md)
- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md)
- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md)

#### Overview

Use an instance of this class to manage a queue of player items.

## Topics

### Creating a queue player
- [init(items: [AVPlayerItem])](avqueueplayer/init(items:).md)
  Creates an object that plays a queue of items.
### Managing the player queue
- [func items() -> [AVPlayerItem]](avqueueplayer/items.md)
  Returns an array of the currently enqueued items.
- [func advanceToNextItem()](avqueueplayer/advancetonextitem.md)
  Ends playback of the current item and starts playback of the next item in the player’s queue.
- [func canInsert(AVPlayerItem, after: AVPlayerItem?) -> Bool](avqueueplayer/caninsert(_:after:).md)
  Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [func insert(AVPlayerItem, after: AVPlayerItem?)](avqueueplayer/insert(_:after:).md)
  Inserts a player item after another player item in the queue.
- [func remove(AVPlayerItem)](avqueueplayer/remove(_:).md)
  Removes a given player item from the queue.
- [func removeAllItems()](avqueueplayer/removeallitems.md)
  Removes all player items from the queue.

## Relationships

### Inherits From
- [AVPlayer](avplayer.md)
### Conforms To
- [AVRoutingPlaybackParticipant](../AVRouting/AVRoutingPlaybackParticipant.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md)
  Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md)
  Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [class AVPlayer](avplayer.md)
  An object that provides the interface to control the player’s transport behavior.
- [class AVPlayerItem](avplayeritem.md)
  An object that models the timing and presentation state of an asset during playback.
- [class AVPlayerItemTrack](avplayeritemtrack.md)
  An object that represents the presentation state of an asset track during playback.
- [class AVPlayerLooper](avplayerlooper.md)
  An object that loops media content using a queue player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer)*