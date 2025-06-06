# SCNParticleEvent.death

**Framework**: SceneKit  
**Kind**: case

Occurs when particles reach the end of their life span.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

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