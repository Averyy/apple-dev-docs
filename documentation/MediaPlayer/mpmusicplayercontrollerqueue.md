# MPMusicPlayerControllerQueue

**Framework**: Media Player  
**Kind**: class

An immutable queue containing the media items to play.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerControllerQueue
```

#### Overview

An `MPMusicPlayerControllerQueue` object contains the current queue for an application queue music player. To add or remove media items from a playing queue, use [`perform(queueTransaction:completionHandler:)`](mpmusicplayerapplicationcontroller/perform(queuetransaction:completionhandler:).md). The results of the method is an `MPMusicPlayerControllerQueue` object that updates the playing queue. You don’t create your own instance of this class.

## Topics

### Inspecting queue media items
- [var items: [MPMediaItem]](mpmusicplayercontrollerqueue/items.md)
  The media items in the queue.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPMusicPlayerControllerMutableQueue](mpmusicplayercontrollermutablequeue.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPMusicPlayerControllerMutableQueue](mpmusicplayercontrollermutablequeue.md)
  A mutable queue containing the media items to play.
- [class MPMusicPlayerApplicationController](mpmusicplayerapplicationcontroller.md)
  A media player object that you use to revise the queue that’s currently playing.
- [class MPMusicPlayerMediaItemQueueDescriptor](mpmusicplayermediaitemqueuedescriptor.md)
  A set of properties and methods for modifying audio media items in the player’s media queue.
- [class MPMusicPlayerStoreQueueDescriptor](mpmusicplayerstorequeuedescriptor.md)
  A set of properties and methods for modifying items, based on their store identifier, in the player’s queue.
- [class MPMusicPlayerPlayParametersQueueDescriptor](mpmusicplayerplayparametersqueuedescriptor.md)
  A set of properties and methods for modifying how to play items, based on play parameters the framework returns.
- [class MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
  The abstract base class for audio media item and store queue descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollerqueue)*