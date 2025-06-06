# MPMusicPlayerControllerMutableQueue

**Framework**: Media Player  
**Kind**: class

A mutable queue containing the media items to play.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerControllerMutableQueue
```

## Topics

### Adding and removing items
- [func insert(MPMusicPlayerQueueDescriptor, after: MPMediaItem?)](mpmusicplayercontrollermutablequeue/insert(_:after:).md)
  Inserts a modified queue after the designated media item.
- [func remove(MPMediaItem)](mpmusicplayercontrollermutablequeue/remove(_:).md)
  Removes a media item from the music player’s queue.

## Relationships

### Inherits From
- [MPMusicPlayerControllerQueue](mpmusicplayercontrollerqueue.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPMusicPlayerControllerQueue](mpmusicplayercontrollerqueue.md)
  An immutable queue containing the media items to play.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollermutablequeue)*