# presentationScreenSize

**Framework**: RealityKit  
**Kind**: property

The size of the screen presenting the image, with the format [width, height] in meters.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var presentationScreenSize: SIMD2<Float> { get }
```

#### Discussion

For immersive viewing modes (`.spatialStereoImmersive` and `.spatial3DImmersive`), this property represents the screen size of the non-immersive version of that mode (`.spatialStereo` and `.spatial3D` respectively).

This property is expressed relative to the local coordinate space of the entity the `ImagePresentationComponent` is assigned to. To calculate the size of the screen in world coordinate space, multiply `presentationScreenSize` by the entity’s world scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/presentationscreensize)*