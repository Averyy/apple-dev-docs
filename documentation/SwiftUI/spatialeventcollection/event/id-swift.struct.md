# SpatialEventCollection.Event.ID

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Identifying the event
- [var timestamp: TimeInterval](./timestamp.md)
  The time the event was processed.
- [var id: SpatialEventCollection.Event.ID](./id-swift.property.md)
  An identifier that uniquely identifies the event over its lifetime.
- [var kind: SpatialEventCollection.Event.Kind](./kind-swift.property.md)
  The event’s input source.
- [SpatialEventCollection.Event.Kind](./kind-swift.enum.md)
  The possible input sources or modes of an event.
- [var modifierKeys: EventModifiers](./modifierkeys.md)
  The set of active modifier keys at the time of this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/id-swift.struct)*