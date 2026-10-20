# SCNParticleEvent

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Significant events in the life spans of simulate particles, used by the [`handle(_:forProperties:handler:)`](./scnparticlesystem/handle%28_,forproperties,handler%29.md) method.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNParticleEvent
```

```c
enum SCNParticleEvent : NSInteger;
```

## Topics

### Constants
- [SCNParticleEvent.birth](./scnparticleevent/birth.md)
  Occurs when new particles spawn.
- [SCNParticleEvent.death](./scnparticleevent/death.md)
  Occurs when particles reach the end of their life span.
- [SCNParticleEvent.collision](./scnparticleevent/collision.md)
  Occurs when particles collide with scene geometry.
### Initializers
- [init?(rawValue: Int)](./scnparticleevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Modifying Particles in Response to Particle System Events
- [func handle(SCNParticleEvent, forProperties: [SCNParticleSystem.ParticleProperty], handler: SCNParticleEventBlock)](./scnparticlesystem/handle%28_,forproperties,handler%29.md)
  Adds a block that modifies particle properties, to be executed at a specified event in the lifetimes of particles in the system.
- [typealias SCNParticleEventBlock](./scnparticleeventblock.md)
  The signature for blocks called by SceneKit in response to significant events during particle simulation, used by the [`handle(_:forProperties:handler:)`](./scnparticlesystem/handle%28_,forproperties,handler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleevent)*