# SCNParticleOrientationMode.free

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Particle orientations are not restricted; they may rotate freely in all axes.

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
case free
```

```c
SCNParticleOrientationModeFree
```

## Discussion

When using this mode, you can modify the rotation axis of each particle with the [`rotationAxis`](../scnparticlesystem/particleproperty/rotationaxis.md) key.

## See Also

### Constants
- [SCNParticleOrientationMode.billboardScreenAligned](./billboardscreenaligned.md)
  Each particle’s orientation is always fixed with respect to the point of view camera.
- [SCNParticleOrientationMode.billboardViewAligned](./billboardviewaligned.md)
  Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).
- [SCNParticleOrientationMode.billboardYAligned](./billboardyaligned.md)
  The y-axis direction of each particle is always fixed with respect to the point of view camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/free)*