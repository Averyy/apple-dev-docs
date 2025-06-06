# SCNParticleOrientationMode.billboardViewAligned

**Framework**: SceneKit  
**Kind**: case

Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).

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
case billboardViewAligned
```

#### Discussion

Use this mode for particle images whose individual appearance depends on a location and orientation in scene space, such as “impostor” images representing trees or clouds in a scene.

## See Also

- [SCNParticleOrientationMode.billboardScreenAligned](scnparticleorientationmode/billboardscreenaligned.md)
  Each particle’s orientation is always fixed with respect to the point of view camera.
- [SCNParticleOrientationMode.free](scnparticleorientationmode/free.md)
  Particle orientations are not restricted; they may rotate freely in all axes.
- [SCNParticleOrientationMode.billboardYAligned](scnparticleorientationmode/billboardyaligned.md)
  The y-axis direction of each particle is always fixed with respect to the point of view camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode/billboardviewaligned)*