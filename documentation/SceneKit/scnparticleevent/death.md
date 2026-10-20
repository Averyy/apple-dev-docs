# SCNParticleEvent.death

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Occurs when particles reach the end of their life span.

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
case death
```

```c
SCNParticleEventDeath
```

#### Discussion

SceneKit calls your event handler block immediately before removing dead particles from the scene.

## See Also

### Constants
- [SCNParticleEvent.birth](./birth.md)
  Occurs when new particles spawn.
- [SCNParticleEvent.collision](./collision.md)
  Occurs when particles collide with scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleevent/death)*