# SCNParticleEvent.death

**Framework**: SceneKit  
**Kind**: case

Occurs when particles reach the end of their life span.

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
case death
```

#### Discussion

SceneKit calls your event handler block immediately before removing dead particles from the scene.

## See Also

- [SCNParticleEvent.birth](scnparticleevent/birth.md)
  Occurs when new particles spawn.
- [SCNParticleEvent.collision](scnparticleevent/collision.md)
  Occurs when particles collide with scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleevent/death)*