# SpatialEventCollection

**Framework**: SwiftUI  
**Kind**: struct

A collection of spatial input events that target a specific view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct SpatialEventCollection
```

#### Overview

You receive a structure of this type as an input to the [`onChanged(_:)`](gesture/onchanged(_:).md) or [`onEnded(_:)`](gesture/onended(_:).md) method of a [`SpatialEventGesture`](spatialeventgesture.md). The structure contains a collection of [`SpatialEventCollection.Event`](spatialeventcollection/event.md) values that correspond to ongoing input events. You can look up a specific event in the collection by its [`id`](spatialeventcollection/event/id-swift.property.md) value or iterate over all events in the collection to apply logic depending on the event’s state.

## Topics

### Accessing the collection’s events
- [SpatialEventCollection.Event](spatialeventcollection/event.md)
  A spatial event generated from an input like a touch or click that can drive gestures in the system.
- [subscript(SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event?](spatialeventcollection/subscript(_:).md)
  Retrieves an event using its unique identifier.
### Iterating over events in the collection
- [func makeIterator() -> SpatialEventCollection.Iterator](spatialeventcollection/makeiterator.md)
  Makes an iterator over all events in the collection.
- [SpatialEventCollection.Iterator](spatialeventcollection/iterator.md)
  An iterator over all events in the collection.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct SpatialEventGesture](spatialeventgesture.md)
  A gesture that provides information about ongoing spatial events like clicks and touches.
- [enum Chirality](chirality.md)
  The chirality, or handedness, of a pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection)*