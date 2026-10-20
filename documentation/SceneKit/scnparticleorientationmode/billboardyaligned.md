# SCNParticleOrientationMode.billboardYAligned

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The y-axis direction of each particle is always fixed with respect to the point of view camera.

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
case billboardYAligned
```

```c
SCNParticleOrientationModeBillboardYAligned
```

#### Discussion

Use this mode to allow each particle to rotate freely about its y-axis (as determined by the [`particleAngle`](../scnparticlesystem/particleangle.md) and [`particleAngularVelocity`](../scnparticlesystem/particleangularvelocity.md) properties or the [`angle`](../scnparticlesystem/particleproperty/angle.md) key), but prevent it from rotating around any other axis.

## See Also

### Constants
- [SCNParticleOrientationMode.billboardScreenAligned](./billboardscreenaligned.md)
  Each particle’s orientation is always fixed with respect to the point of view camera.
- [SCNParticleOrientationMode.billboardViewAligned](./billboardviewaligned.md)
  Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).
- [SCNParticleOrientationMode.free](./free.md)
  Particle orientations are not restricted; they may rotate freely in all axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/billboardyaligned)*