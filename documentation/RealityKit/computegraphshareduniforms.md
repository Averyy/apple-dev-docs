# ComputeGraphSharedUniforms

**Framework**: RealityKit  
**Kind**: class

A transient component that stores typed uniform values shared across all ComputeGraph simulations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class ComputeGraphSharedUniforms
```

#### Overview

You add scene-wide uniforms via a `ComputeGraphSharedUniforms` — such as gravity, wind, attractor locations, or a global time offset.

> **Note**: Only one instance of this component should exist in a scene at a time.

## Topics

### Initializers
- [init()](computegraphshareduniforms/init.md)
  Creates an empty `ComputeGraphSharedUniforms` component.
### Instance Methods
- [func setUniform<V>(borrowing V)](computegraphshareduniforms/setuniform(_:).md)
  Stores a uniform value, replacing any previously stored value of the same type.
- [func setUniformTransform<V>((V, Entity) -> V)](computegraphshareduniforms/setuniformtransform(_:).md)
  Registers a closure that transforms a uniform value of type `V` on a per-entity basis.
- [func setUniformTransform<V>(type: V.Type, transform: (inout MutableRawSpan, Entity) -> Void)](computegraphshareduniforms/setuniformtransform(type:transform:).md)
  Registers a raw-data transformer closure for a uniform of type `V`.
- [func uniform<V>(V.Type) -> V?](computegraphshareduniforms/uniform(_:).md)
  Returns the stored uniform value for the given type, or `nil` if none has been set.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphshareduniforms)*