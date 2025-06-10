# screenImageDimension

**Framework**: RealityKit  
**Kind**: property

The image resolution of the currently presented image, in pixels.

**Availability**:
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/screenimagedimension)*