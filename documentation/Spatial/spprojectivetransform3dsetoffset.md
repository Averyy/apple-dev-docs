# SPProjectiveTransform3DSetOffset

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Sets the translation of a projective transform.

**Availability**:
- iOS 16.0+ - Deprecated in 16.0
- iPadOS 16.0+ - Deprecated in 16.0
- Mac Catalyst 16.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 13.0
- tvOS 16.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 9.0

## Declaration

```c
static void SPProjectiveTransform3DSetOffset(SPProjectiveTransform3D *transform, SPVector3D offset);
```

## See Also

### Deprecated symbols
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double, reverseZ: Bool)](./projectivetransform3d/init%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Returns a projective transform with right-hand-side perspective and optional reverse-z.
- [init(fovyRadians: Double, aspectRatio: Double, nearZ: Double, farZ: Double)](./projectivetransform3d/init%28fovyradians,aspectratio,nearz,farz%29.md)
- [SPProjectiveTransform3DMakeTranslation](./spprojectivetransform3dmaketranslation-5hc37.md)
  Creates a projective transform from the specified translate transform.
- [SPProjectiveTransform3DMakeWithRHPerspective](./spprojectivetransform3dmakewithrhperspective-97qwp.md)
  Returns a projective transform with right-hand side perspective.
- [SPProjectiveTransform3DTranslate](./spprojectivetransform3dtranslate-4tynj.md)
  Returns a transform with an origin that’s offset by the specified size.
- [SPProjectiveTransform3DGetTranslation](./spprojectivetransform3dgettranslation.md)
  The projective transform’s translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dsetoffset)*