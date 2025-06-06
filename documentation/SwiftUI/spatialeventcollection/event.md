# SpatialEventCollection.Event

**Framework**: SwiftUI  
**Kind**: struct

A spatial event generated from an input like a touch or click that can drive gestures in the system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct Event
```

#### Overview

You receive a collection of these events in the form of a [`SpatialEventCollection`](spatialeventcollection.md) that’s the input to the [`onChanged(_:)`](gesture/onchanged(_:).md) or [`onEnded(_:)`](gesture/onended(_:).md) method of a [`SpatialEventGesture`](spatialeventgesture.md). Inspect individual events to track interactions that enable you to create complex, multi-touch experiences in your app.

## Topics

### Identifying the event
- [var timestamp: TimeInterval](spatialeventcollection/event/timestamp.md)
  The time the event was processed.
- [var id: SpatialEventCollection.Event.ID](spatialeventcollection/event/id-swift.property.md)
  An identifier that uniquely identifies the event over its lifetime.
- [SpatialEventCollection.Event.ID](spatialeventcollection/event/id-swift.struct.md)
  A value that uniquely identifies an event over the course of its lifetime.
- [var kind: SpatialEventCollection.Event.Kind](spatialeventcollection/event/kind-swift.property.md)
  The event’s input source.
- [SpatialEventCollection.Event.Kind](spatialeventcollection/event/kind-swift.enum.md)
  The possible input sources or modes of an event.
- [var modifierKeys: EventModifiers](spatialeventcollection/event/modifierkeys.md)
  The set of active modifier keys at the time of this event.
### Locating the event
- [var location: CGPoint](spatialeventcollection/event/location.md)
  The 2D location of the event.
- [var location3D: Point3D](spatialeventcollection/event/location3d.md)
  The 3D location of the touch.
- [var selectionRay: Ray3D?](spatialeventcollection/event/selectionray.md)
  The 3D ray used to target the touch.
- [var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?](spatialeventcollection/event/inputdevicepose-swift.property.md)
  The 3D position and orientation of the device controlling the touch, if one exists.
- [SpatialEventCollection.Event.InputDevicePose](spatialeventcollection/event/inputdevicepose-swift.struct.md)
  A pose describing the input device like a hand controlling the event.
- [var targetedEntity: Entity?](spatialeventcollection/event/targetedentity.md)
  The entity target for this touch, if one exists.
### Getting the event’s current phase
- [var phase: SpatialEventCollection.Event.Phase](spatialeventcollection/event/phase-swift.property.md)
  The phase of the event.
- [SpatialEventCollection.Event.Phase](spatialeventcollection/event/phase-swift.enum.md)
  The states that an event can have.
### Instance Properties
- [var chirality: Chirality?](spatialeventcollection/event/chirality.md)
  The hand chirality (left or right) of this event, for relevant event kinds.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [subscript(SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event?](spatialeventcollection/subscript(_:).md)
  Retrieves an event using its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event)*