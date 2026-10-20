# SpatialEventCollection.Event.Kind

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The possible input sources or modes of an event.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum Kind
```

## Topics

### Getting the event type
- [SpatialEventCollection.Event.Kind.directPinch](./kind-swift.enum/directpinch.md)
  An event generated from a pinching hand in close proximity to content.
- [SpatialEventCollection.Event.Kind.indirectPinch](./kind-swift.enum/indirectpinch.md)
  An event generated from an indirectly targeted pinching hand.
- [SpatialEventCollection.Event.Kind.pointer](./kind-swift.enum/pointer.md)
  An event representing a click-based, indirect input device describing the input sequence from click to click release.
- [SpatialEventCollection.Event.Kind.touch](./kind-swift.enum/touch.md)
  An event generated from a touch directly targeting content.
### Enumeration Cases
- [SpatialEventCollection.Event.Kind.pencil](./kind-swift.enum/pencil.md)
  An event generated from a pencil making contact with content.

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
- [SpatialEventCollection.Event.ID](./id-swift.struct.md)
  A value that uniquely identifies an event over the course of its lifetime.
- [var kind: SpatialEventCollection.Event.Kind](./kind-swift.property.md)
  The event’s input source.
- [var modifierKeys: EventModifiers](./modifierkeys.md)
  The set of active modifier keys at the time of this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/kind-swift.enum)*