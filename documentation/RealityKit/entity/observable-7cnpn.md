# Entity.Observable

**Framework**: RealityKit  
**Kind**: struct

When properties in `Entity.Observable` are accessed, they participate in Observation. This means that when they change, any observers will be notified. Each of its properties passes through to the underlying Entity’s corresponding properties, so modifications of them will modify the underlying Entity’s corresponding property.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
struct Observable
```

## Topics

### Structures
- [Entity.Observable.Components](entity/observable-7cnpn/components-swift.struct.md)
  All the components that an entity stores.
### Instance Properties
- [var children: Entity.ChildCollection](entity/observable-7cnpn/children.md)
- [var components: Entity.Observable.Components](entity/observable-7cnpn/components-swift.property.md)
  A “pass through” to the underlying ComponentSet but with the added effect of marking those component keypaths as “accessed” when a property is read. Mutations to any accessed components will cause any observers to be triggered.
- [var isEnabled: Bool](entity/observable-7cnpn/isenabled.md)
- [var name: String](entity/observable-7cnpn/name.md)
- [var orientation: simd_quatf](entity/observable-7cnpn/orientation.md)
- [var position: SIMD3<Float>](entity/observable-7cnpn/position.md)
- [var scale: SIMD3<Float>](entity/observable-7cnpn/scale.md)
- [var transform: Transform](entity/observable-7cnpn/transform.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/observable-7cnpn)*