# MPMusicPlayerPlayParametersQueueDescriptor

**Framework**: Media Player  
**Kind**: class

A set of properties and methods for modifying how to play items, based on play parameters the framework returns.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerPlayParametersQueueDescriptor
```

#### Overview

Use this class to modify the player queue created by a query before the queue begins to play. You can modify when individual items start and stop playing, along with setting the first item for playing.

## Topics

### Creating a new play parameters queue descriptor
- [init(playParametersQueue: [MPMusicPlayerPlayParameters])](mpmusicplayerplayparametersqueuedescriptor/init(playparametersqueue:).md)
  Creates a new queue descriptor using the designated queue of play parameters.
- [class MPMusicPlayerPlayParameters](mpmusicplayerplayparameters.md)
  The MusicKit parameters that describe items to play.
### Accessing the play parameters
- [var playParametersQueue: [MPMusicPlayerPlayParameters]](mpmusicplayerplayparametersqueuedescriptor/playparametersqueue.md)
  An array containing the play parameters returned from querying MusicKit.
- [var startItemPlayParameters: MPMusicPlayerPlayParameters?](mpmusicplayerplayparametersqueuedescriptor/startitemplayparameters.md)
  The item identified by the play parameters to play first.
- [class MPMusicPlayerPlayParameters](mpmusicplayerplayparameters.md)
  The MusicKit parameters that describe items to play.
### Setting start and end times
- [func setStartTime(TimeInterval, forItemWith: MPMusicPlayerPlayParameters)](mpmusicplayerplayparametersqueuedescriptor/setstarttime(_:foritemwith:).md)
  Sets the time the item with the associated play parameters is to start playing.
- [func setEndTime(TimeInterval, forItemWith: MPMusicPlayerPlayParameters)](mpmusicplayerplayparametersqueuedescriptor/setendtime(_:foritemwith:).md)
  Sets the time the item with the associated play parameters is to stop playing.

## Relationships

### Inherits From
- [MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
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
- [class MPMusicPlayerControllerMutableQueue](mpmusicplayercontrollermutablequeue.md)
  A mutable queue containing the media items to play.
- [class MPMusicPlayerApplicationController](mpmusicplayerapplicationcontroller.md)
  A media player object that you use to revise the queue that’s currently playing.
- [class MPMusicPlayerMediaItemQueueDescriptor](mpmusicplayermediaitemqueuedescriptor.md)
  A set of properties and methods for modifying audio media items in the player’s media queue.
- [class MPMusicPlayerStoreQueueDescriptor](mpmusicplayerstorequeuedescriptor.md)
  A set of properties and methods for modifying items, based on their store identifier, in the player’s queue.
- [class MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
  The abstract base class for audio media item and store queue descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor)*