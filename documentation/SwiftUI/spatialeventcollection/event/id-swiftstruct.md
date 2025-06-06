# SpatialEventCollection.Event.ID

**Framework**: SwiftUI  
**Kind**: struct

A value that uniquely identifies an event over the course of its lifetime.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct ID
```

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var timestamp: TimeInterval](spatialeventcollection/event/timestamp.md)
  The time the event was processed.
- [var id: SpatialEventCollection.Event.ID](spatialeventcollection/event/id-swift.property.md)
  An identifier that uniquely identifies the event over its lifetime.
- [var kind: SpatialEventCollection.Event.Kind](spatialeventcollection/event/kind-swift.property.md)
  The event’s input source.
- [SpatialEventCollection.Event.Kind](spatialeventcollection/event/kind-swift.enum.md)
  The possible input sources or modes of an event.
- [var modifierKeys: EventModifiers](spatialeventcollection/event/modifierkeys.md)
  The set of active modifier keys at the time of this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/id-swift.struct)*