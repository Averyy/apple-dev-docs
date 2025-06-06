# SCNParticleOrientationMode.free

**Framework**: SceneKit  
**Kind**: case

Particle orientations are not restricted; they may rotate freely in all axes.

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
case free
```

#### Discussion

When using this mode, you can modify the rotation axis of each particle with the [`rotationAxis`](scnparticlesystem/particleproperty/rotationaxis.md) key.

## See Also

- [SCNParticleOrientationMode.billboardScreenAligned](scnparticleorientationmode/billboardscreenaligned.md)
  Each particle’s orientation is always fixed with respect to the point of view camera.
- [SCNParticleOrientationMode.billboardViewAligned](scnparticleorientationmode/billboardviewaligned.md)
  Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).
- [SCNParticleOrientationMode.billboardYAligned](scnparticleorientationmode/billboardyaligned.md)
  The y-axis direction of each particle is always fixed with respect to the point of view camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/free)*