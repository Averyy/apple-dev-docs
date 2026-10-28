# SpatialEventCollection.Event

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

You receive a collection of these events in the form of a [`SpatialEventCollection`](../spatialeventcollection.md) that’s the input to the [`onChanged(_:)`](../gesture/onchanged%28_%29.md) or [`onEnded(_:)`](../gesture/onended%28_%29.md) method of a [`SpatialEventGesture`](../spatialeventgesture.md). Inspect individual events to track interactions that enable you to create complex, multi-touch experiences in your app.

## Topics

### Identifying the event
- [var timestamp: TimeInterval](./event/timestamp.md)
  The time the event was processed.
- [var id: SpatialEventCollection.Event.ID](./event/id-swift.property.md)
  An identifier that uniquely identifies the event over its lifetime.
- [SpatialEventCollection.Event.ID](./event/id-swift.struct.md)
  A value that uniquely identifies an event over the course of its lifetime.
- [var kind: SpatialEventCollection.Event.Kind](./event/kind-swift.property.md)
  The event’s input source.
- [SpatialEventCollection.Event.Kind](./event/kind-swift.enum.md)
  The possible input sources or modes of an event.
- [var modifierKeys: EventModifiers](./event/modifierkeys.md)
  The set of active modifier keys at the time of this event.
### Locating the event
- [var location: CGPoint](./event/location.md)
  The 2D location of the event.
- [var location3D: Point3D](./event/location3d.md)
  The 3D location of the touch.
- [var selectionRay: Ray3D?](./event/selectionray.md)
  The 3D ray used to target the touch.
- [var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?](./event/inputdevicepose-swift.property.md)
  The 3D position and orientation of the device controlling the touch, if one exists.
- [SpatialEventCollection.Event.InputDevicePose](./event/inputdevicepose-swift.struct.md)
  A pose describing the input device like a hand controlling the event.
- [var targetedEntity: Entity?](./event/targetedentity.md)
  The entity target for this touch, if one exists.
### Getting the event’s current phase
- [var phase: SpatialEventCollection.Event.Phase](./event/phase-swift.property.md)
  The phase of the event.
- [SpatialEventCollection.Event.Phase](./event/phase-swift.enum.md)
  The states that an event can have.
### Instance Properties
- [var chirality: Chirality?](./event/chirality.md)
  The hand chirality (left or right) of this event, for relevant event kinds.
- [var trackingAreaIdentifier: LayerRenderer.Drawable.TrackingArea.Identifier](./event/trackingareaidentifier.md)
  The tracking area identifier of the event, if the gesture is attached to a `CompositorLayer`, or `nil` if the event didn’t hit a tracking area or the gesture isn’t attached to a `CompositorLayer`.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Accessing the collection’s events
- [subscript(SpatialEventCollection.Event.ID) -> SpatialEventCollection.Event?](./subscript%28_%29.md)
  Retrieves an event using its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event)*