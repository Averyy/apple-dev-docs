# AVQueuePlayer

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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
class AVQueuePlayer
```

```objc
@interface AVQueuePlayer : AVPlayer
```

## Mentions

- [Implementing simple enhanced buffering for your content](./implementing-simple-enhanced-buffering-for-your-content.md)
- [Observing playback state in SwiftUI](./observing-playback-state-in-swiftui.md)
- [Supporting AirPlay in your app](./supporting-airplay-in-your-app.md)

#### Overview

Use an instance of this class to manage a queue of player items.

## Topics

### Creating a queue player
- [init(items: [AVPlayerItem])](./avqueueplayer/init%28items%29.md)
  Creates an object that plays a queue of items.
### Managing the player queue
- [func items() -> [AVPlayerItem]](./avqueueplayer/items%28%29.md)
  Returns an array of the currently enqueued items.
- [func advanceToNextItem()](./avqueueplayer/advancetonextitem%28%29.md)
  Ends playback of the current item and starts playback of the next item in the player’s queue.
- [func canInsert(AVPlayerItem, after: AVPlayerItem?) -> Bool](./avqueueplayer/caninsert%28_,after%29.md)
  Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [func insert(AVPlayerItem, after: AVPlayerItem?)](./avqueueplayer/insert%28_,after%29.md)
  Inserts a player item after another player item in the queue.
- [func remove(AVPlayerItem)](./avqueueplayer/remove%28_%29.md)
  Removes a given player item from the queue.
- [func removeAllItems()](./avqueueplayer/removeallitems%28%29.md)
  Removes all player items from the queue.

## Relationships

### Inherits From
- [AVPlayer](./avplayer.md)
### Conforms To
- [AVRoutingPlaybackParticipant](../AVRouting/avroutingplaybackparticipant.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Playback control
- [Observing playback state in SwiftUI](./observing-playback-state-in-swiftui.md)
  Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](./controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](./creating-a-seamless-multiview-playback-experience.md)
  Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [class AVPlayer](./avplayer.md)
  An object that provides the interface to control the player’s transport behavior.
- [class AVPlayerItem](./avplayeritem.md)
  An object that models the timing and presentation state of an asset during playback.
- [class AVPlayerItemTrack](./avplayeritemtrack.md)
  An object that represents the presentation state of an asset track during playback.
- [class AVPlayerLooper](./avplayerlooper.md)
  An object that loops media content using a queue player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueueplayer)*