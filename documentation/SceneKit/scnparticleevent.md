# SCNParticleEvent

**Framework**: SceneKit  
**Kind**: enum

Significant events in the life spans of simulate particles, used by the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.

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
enum SCNParticleEvent
```

## Topics

### Constants
- [SCNParticleEvent.birth](scnparticleevent/birth.md)
  Occurs when new particles spawn.
- [SCNParticleEvent.death](scnparticleevent/death.md)
  Occurs when particles reach the end of their life span.
- [SCNParticleEvent.collision](scnparticleevent/collision.md)
  Occurs when particles collide with scene geometry.
### Initializers
- [init?(rawValue: Int)](scnparticleevent/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func handle(SCNParticleEvent, forProperties: [SCNParticleSystem.ParticleProperty], handler: SCNParticleEventBlock)](scnparticlesystem/handle(_:forproperties:handler:).md)
  Adds a block that modifies particle properties, to be executed at a specified event in the lifetimes of particles in the system.
- [typealias SCNParticleEventBlock](scnparticleeventblock.md)
  The signature for blocks called by SceneKit in response to significant events during particle simulation, used by the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleevent)*