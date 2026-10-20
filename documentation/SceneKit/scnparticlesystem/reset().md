# reset()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the particle system to its initial state.

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
func reset()
```

```objc
- (void) reset;
```

#### Discussion

Calling this method removes all currently live particles from the scene.

## See Also

### Controlling Particle Simulation
- [var isLocal: Bool](./islocal.md)
  A Boolean value that specifies whether the particle simulation runs in the local coordinate space of the node containing it.
- [var speedFactor: CGFloat](./speedfactor.md)
  A multiplier for the speed at which SceneKit runs the particle simulation. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/reset())*