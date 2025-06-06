# MPMusicPlayerApplicationController

**Framework**: Media Player  
**Kind**: class

A media player object that you use to revise the queue that’s currently playing.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerApplicationController
```

## Topics

### Changing the queue contents
- [func perform(queueTransaction: (MPMusicPlayerControllerMutableQueue) -> Void, completionHandler: (MPMusicPlayerControllerQueue, (any Error)?) -> Void)](mpmusicplayerapplicationcontroller/perform(queuetransaction:completionhandler:).md)
  Changes the contents of the media items in the queue.
- [static let MPMusicPlayerControllerQueueDidChange: NSNotification.Name](../foundation/nsnotification/name/2815063-mpmusicplayercontrollerqueuedidc.md)
  Indicates the music player’s queue changed.

## Relationships

### Inherits From
- [MPMusicPlayerController](mpmusicplayercontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPMediaPlayback](mpmediaplayback.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPMusicPlayerControllerQueue](mpmusicplayercontrollerqueue.md)
  An immutable queue containing the media items to play.
- [class MPMusicPlayerControllerMutableQueue](mpmusicplayercontrollermutablequeue.md)
  A mutable queue containing the media items to play.
- [class MPMusicPlayerMediaItemQueueDescriptor](mpmusicplayermediaitemqueuedescriptor.md)
  A set of properties and methods for modifying audio media items in the player’s media queue.
- [class MPMusicPlayerStoreQueueDescriptor](mpmusicplayerstorequeuedescriptor.md)
  A set of properties and methods for modifying items, based on their store identifier, in the player’s queue.
- [class MPMusicPlayerPlayParametersQueueDescriptor](mpmusicplayerplayparametersqueuedescriptor.md)
  A set of properties and methods for modifying how to play items, based on play parameters the framework returns.
- [class MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
  The abstract base class for audio media item and store queue descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerapplicationcontroller)*