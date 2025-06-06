# targetedToEntity(_:)

**Framework**: SwiftUI  
**Kind**: method

Requires this gesture to target an entity or a descendant of entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func targetedToEntity(_ entity: Entity) -> some Gesture<EntityTargetValue<Self.Value>>
```

#### Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture value along with the targeted entity.

## Parameters

- `entity`: The entity the gesture targets.

## See Also

- [func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>
](gesture/targetedtoanyentity.md)
  Requires this gesture to target an entity.
- [func targetedToEntity(where: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>
](gesture/targetedtoentity(where:).md)
  Requires this gesture to target an entity that can be found in the results of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/targetedtoentity(_:))*