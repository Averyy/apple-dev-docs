# SCNParticleOrientationMode.billboardScreenAligned

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Each particle’s orientation is always fixed with respect to the point of view camera.

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
case billboardScreenAligned
```

```c
SCNParticleOrientationModeBillboardScreenAligned
```

#### Discussion

Use this mode for simple particle images whose individual appearance has no relation to scene space, such as spheres, circles, and “sparkle” artwork.

## See Also

### Constants
- [SCNParticleOrientationMode.billboardViewAligned](./billboardviewaligned.md)
  Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).
- [SCNParticleOrientationMode.free](./free.md)
  Particle orientations are not restricted; they may rotate freely in all axes.
- [SCNParticleOrientationMode.billboardYAligned](./billboardyaligned.md)
  The y-axis direction of each particle is always fixed with respect to the point of view camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/billboardscreenaligned)*