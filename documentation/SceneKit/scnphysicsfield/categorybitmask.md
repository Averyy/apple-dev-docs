# categoryBitMask

**Framework**: SceneKit  
**Kind**: property

A mask that defines which categories this physics field belongs to.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var categoryBitMask: Int { get set }
```

#### Discussion

To determine whether a field affects a physics body, SceneKit performs a bitwise AND operation on the field’s category bit mask and the body’s [`categoryBitMask`](scnphysicsbody/categorybitmask.md) property. If the result is a nonzero value, SceneKit computes and applies the force of the field on the body. To determine whether a field affects the particles spawned by an [`SCNParticleSystem`](scnparticlesystem.md) object, SceneKit performs the same check using the [`categoryBitMask`](scnnode/categorybitmask.md) property of the node containing the particle system.

Use this property to create fields which affect only certain bodies in your scene. Reducing the number of bodies affected by fields can also improve simulation performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/categorybitmask)*