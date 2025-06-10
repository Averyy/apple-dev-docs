# reset()

**Framework**: SceneKit  
**Kind**: method

Returns the particle system to its initial state.

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
func reset()
```

#### Discussion

Calling this method removes all currently live particles from the scene.

## See Also

- [var isLocal: Bool](scnparticlesystem/islocal.md)
  A Boolean value that specifies whether the particle simulation runs in the local coordinate space of the node containing it.
- [var speedFactor: CGFloat](scnparticlesystem/speedfactor.md)
  A multiplier for the speed at which SceneKit runs the particle simulation. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/reset())*