# targetedToAnyEntity()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Requires this gesture to target an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>
```

## Return Value

A `RealityCoordinateSpaceConvertible`value containing the original gesture value along with the targeted entity.

## See Also

### Using a gesture with a RealityKit entity
- [func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
](./targetedtoentity%28_%29.md)
  Requires this gesture to target an entity or a descendant of entity.
- [func targetedToEntity(where: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>
](./targetedtoentity%28where%29.md)
  Requires this gesture to target an entity that can be found in the results of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/targetedtoanyentity())*