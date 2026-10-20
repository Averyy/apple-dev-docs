# SCNParticleEvent.collision

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Occurs when particles collide with scene geometry.

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
case collision
```

```c
SCNParticleEventCollision
```

#### Discussion

SceneKit calls your event handler block immediately after resolving the collision.

## See Also

### Constants
- [SCNParticleEvent.birth](./birth.md)
  Occurs when new particles spawn.
- [SCNParticleEvent.death](./death.md)
  Occurs when particles reach the end of their life span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleevent/collision)*