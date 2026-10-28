# targetedToEntity(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

A `RealityCoordinateSpaceConverting` value containing the original gesture value along with the targeted entity.

## Parameters

- `entity`: The entity the gesture targets.

## See Also

### Using a gesture with a RealityKit entity
- [func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>
](./targetedtoanyentity%28%29.md)
  Requires this gesture to target an entity.
- [func targetedToEntity(where: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>
](./targetedtoentity%28where%29.md)
  Requires this gesture to target an entity that can be found in the results of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/targetedtoentity(_:))*