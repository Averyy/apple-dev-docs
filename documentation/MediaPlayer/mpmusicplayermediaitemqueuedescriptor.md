# MPMusicPlayerMediaItemQueueDescriptor

**Framework**: Media Player  
**Kind**: class

A set of properties and methods for modifying audio media items in the player’s media queue.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerMediaItemQueueDescriptor
```

#### Overview

Use this class to modify the player queue created by a query before the queue begins to play. You can modify when individual items start and stop playing, along with setting the first item to play.

## Topics

### Creating a new media item queue descriptor
- [init(itemCollection: MPMediaItemCollection)](mpmusicplayermediaitemqueuedescriptor/init(itemcollection:).md)
  Creates a new queue descriptor using the designated collection.
- [init(query: MPMediaQuery)](mpmusicplayermediaitemqueuedescriptor/init(query:).md)
  Creates a new queue descriptor using the designated query.
### Media item queue descriptor properties
- [var itemCollection: MPMediaItemCollection](mpmusicplayermediaitemqueuedescriptor/itemcollection.md)
  Contains the media item collection used to create the queue descriptor.
- [var query: MPMediaQuery](mpmusicplayermediaitemqueuedescriptor/query.md)
  Contains the media items found by the query used to create the queue descriptor.
- [var startItem: MPMediaItem?](mpmusicplayermediaitemqueuedescriptor/startitem.md)
  Designates the media item to play first.
### Setting start and end times
- [func setStartTime(TimeInterval, for: MPMediaItem)](mpmusicplayermediaitemqueuedescriptor/setstarttime(_:for:).md)
  The time the designated media item is to start playing.
- [func setEndTime(TimeInterval, for: MPMediaItem)](mpmusicplayermediaitemqueuedescriptor/setendtime(_:for:).md)
  The time the designated media item is to stop playing.

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
- [class MPMusicPlayerStoreQueueDescriptor](mpmusicplayerstorequeuedescriptor.md)
  A set of properties and methods for modifying items, based on their store identifier, in the player’s queue.
- [class MPMusicPlayerPlayParametersQueueDescriptor](mpmusicplayerplayparametersqueuedescriptor.md)
  A set of properties and methods for modifying how to play items, based on play parameters the framework returns.
- [class MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
  The abstract base class for audio media item and store queue descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor)*