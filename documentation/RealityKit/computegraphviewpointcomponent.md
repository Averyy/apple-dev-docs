# ComputeGraphViewpointComponent

**Framework**: RealityKit  
**Kind**: struct

A transient component that provides camera viewpoint information to the particle simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ComputeGraphViewpointComponent
```

#### Overview

Attach this component to an entity to supply the simulation with an observer’s position and direction. The simulation uses these values for view-dependent effects such as billboard orientation or camera-facing particles.

Both properties are optional. When `nil`, the simulation falls back to its default viewpoint behavior.

## Topics

### Initializers
- [init()](computegraphviewpointcomponent/init.md)
### Instance Properties
- [var viewDirection: SIMD3<Float>?](computegraphviewpointcomponent/viewdirection.md)
  The direction the observer is facing, in world space.
- [var viewPosition: SIMD3<Float>?](computegraphviewpointcomponent/viewposition.md)
  The position of the observer, in world space.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphviewpointcomponent)*