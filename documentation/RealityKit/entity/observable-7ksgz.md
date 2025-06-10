# Entity.Observable

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS ?+
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
struct Observable
```

## Topics

### Structures
- [Entity.Observable.Components](entity/observable-7ksgz/components-swift.struct.md)
  All the components that an entity stores.
### Instance Properties
- [var children: Entity.ChildCollection](entity/observable-7ksgz/children.md)
- [var components: Entity.Observable.Components](entity/observable-7ksgz/components-swift.property.md)
  A “pass through” to the underlying ComponentSet but with the added effect of marking those component keypaths as “accessed” when a property is read. Mutations to any accessed components will cause any observers to be triggered.
- [var name: String](entity/observable-7ksgz/name.md)
- [var orientation: simd_quatf](entity/observable-7ksgz/orientation.md)
- [var position: SIMD3<Float>](entity/observable-7ksgz/position.md)
- [var scale: SIMD3<Float>](entity/observable-7ksgz/scale.md)
- [var transform: Transform](entity/observable-7ksgz/transform.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/observable-7ksgz)*