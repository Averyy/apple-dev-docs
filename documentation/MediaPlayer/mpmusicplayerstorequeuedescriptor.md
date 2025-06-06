# MPMusicPlayerStoreQueueDescriptor

**Framework**: Media Player  
**Kind**: class

A set of properties and methods for modifying items, based on their store identifier, in the player’s queue.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerStoreQueueDescriptor
```

#### Overview

Use this class to modify the player queue created by a query before the queue begins to play. You can modify when individual items start and stop playing, along with setting the first item to play.

## Topics

### Creating a new store queue descriptor
- [init(storeIDs: [String])](mpmusicplayerstorequeuedescriptor/init(storeids:).md)
  Creates a new queue descriptor using the designated store identifiers.
### Store identifier queue descriptor properties
- [var startItemID: String?](mpmusicplayerstorequeuedescriptor/startitemid.md)
  The item identified by the store identifier to play first.
- [var storeIDs: [String]?](mpmusicplayerstorequeuedescriptor/storeids.md)
  An array containing the store identifiers found by the query used to create the queue descriptor.
### Setting start and end times
- [func setStartTime(TimeInterval, forItemWithStoreID: String)](mpmusicplayerstorequeuedescriptor/setstarttime(_:foritemwithstoreid:).md)
  Sets the time the designated store item is to start playing.
- [func setEndTime(TimeInterval, forItemWithStoreID: String)](mpmusicplayerstorequeuedescriptor/setendtime(_:foritemwithstoreid:).md)
  Sets the time the designated store item is to stop playing.

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
- [class MPMusicPlayerPlayParametersQueueDescriptor](mpmusicplayerplayparametersqueuedescriptor.md)
  A set of properties and methods for modifying how to play items, based on play parameters the framework returns.
- [class MPMusicPlayerQueueDescriptor](mpmusicplayerqueuedescriptor.md)
  The abstract base class for audio media item and store queue descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor)*