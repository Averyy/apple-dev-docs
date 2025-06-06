# SpatialEventCollection.Event.Phase

**Framework**: SwiftUI  
**Kind**: enum

The states that an event can have.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum Phase
```

## Topics

### Getting the phase
- [SpatialEventCollection.Event.Phase.active](spatialeventcollection/event/phase-swift.enum/active.md)
  The phase is active and the state associated with it is guaranteed to produce at least one more update.
- [SpatialEventCollection.Event.Phase.cancelled](spatialeventcollection/event/phase-swift.enum/cancelled.md)
  The state associated with this phase was canceled and won’t produce any more updates.
- [SpatialEventCollection.Event.Phase.ended](spatialeventcollection/event/phase-swift.enum/ended.md)
  The state associated with this phase ended normally and won’t produce any more updates.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var phase: SpatialEventCollection.Event.Phase](spatialeventcollection/event/phase-swift.property.md)
  The phase of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/phase-swift.enum)*