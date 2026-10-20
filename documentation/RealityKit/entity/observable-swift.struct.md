# Entity.Observable

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An observable interface to an entity’s properties and components, enabling reactive updates using Swift’s Observation framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@frozen
struct Observable
```

#### Overview

When you access properties in this structure, they participate in Observation. This means that the app notifies obersvers when they change in value. Each of these properties passes through to the underlying entity’s corresponding properties, so modifications of them modify the entity’s corresponding property.

## Topics

### Structures
- [Entity.Observable.Components](./observable-swift.struct/components-swift.struct.md)
  An observable collection of an entity’s attached components, allowing for reactive updates based on component changes.
### Instance Properties
- [var children: Entity.ChildCollection](./observable-swift.struct/children.md)
  The collection of child entities, allowing observation of its contents
- [var components: Entity.Observable.Components](./observable-swift.struct/components-swift.property.md)
  The components an entity manages, enabling observation of their presence and values.
- [var isEnabled: Bool](./observable-swift.struct/isenabled.md)
  A Boolean value that indicates whether the entity is enabled in the scene, allowing observation of its state.
- [var name: String](./observable-swift.struct/name.md)
  The entity’s name, enabling observation of its changes.
- [var orientation: simd_quatf](./observable-swift.struct/orientation.md)
  The entity’s local orientation, allowing observation of its rotation.
- [var position: SIMD3<Float>](./observable-swift.struct/position.md)
  The entity’s local position, allowing observation of its translation.
- [var scale: SIMD3<Float>](./observable-swift.struct/scale.md)
  The entity’s local scale, enabling observation of its size.
- [var transform: Transform](./observable-swift.struct/transform.md)
  The entity’s position, rotation, and scale, enabling observation of its complete spatial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/observable-swift.struct)*