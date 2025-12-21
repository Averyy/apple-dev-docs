# screenImageDimension

**Framework**: RealityKit  
**Kind**: property

The image resolution of the currently presented image, in pixels.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var screenImageDimension: SIMD2<Float> { get }
```

#### Discussion

The meaning of this resolution depends on the current viewing mode:

- In monoscopic viewing modes, this property returns the size of the monoscopic image
- In spatial stereo viewing modes, this property returns the size of each image in the spatial stereo pair
- In spatial 3D viewing modes, this property returns the size of the monoscopic image used to generate the spatial 3D resource

This property has the format `[width, height]` in pixels.

## See Also

- [func aspectRatio(for: ImagePresentationComponent.ViewingMode) -> Float?](imagepresentationcomponent/aspectratio(for:).md)
  The aspect ratio of the image this component will present for the requested viewing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/screenimagedimension)*