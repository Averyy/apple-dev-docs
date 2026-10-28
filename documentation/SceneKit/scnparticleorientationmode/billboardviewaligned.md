# SCNParticleOrientationMode.billboardViewAligned

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).

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
case billboardViewAligned
```

```c
SCNParticleOrientationModeBillboardViewAligned
```

## Discussion

Use this mode for particle images whose individual appearance depends on a location and orientation in scene space, such as “impostor” images representing trees or clouds in a scene.

## See Also

### Constants
- [SCNParticleOrientationMode.billboardScreenAligned](./billboardscreenaligned.md)
  Each particle’s orientation is always fixed with respect to the point of view camera.
- [SCNParticleOrientationMode.free](./free.md)
  Particle orientations are not restricted; they may rotate freely in all axes.
- [SCNParticleOrientationMode.billboardYAligned](./billboardyaligned.md)
  The y-axis direction of each particle is always fixed with respect to the point of view camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/billboardviewaligned)*