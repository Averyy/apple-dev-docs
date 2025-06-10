# ImagePresentationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that supports general image presentation.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImagePresentationComponent
```

## Topics

### Classes
- [ImagePresentationComponent.Spatial3DImage](imagepresentationcomponent/spatial3dimage.md)
  A generatable 3D image created from an existing image source.
### Structures
- [ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.struct.md)
  Image content’s rendering mode.
### Initializers
- [init(contentsOf: URL) async throws](imagepresentationcomponent/init(contentsof:).md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image file URL.
- [init(imageSource: CGImageSource) async throws](imagepresentationcomponent/init(imagesource:).md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image source.
- [init(spatial3DImage: ImagePresentationComponent.Spatial3DImage)](imagepresentationcomponent/init(spatial3dimage:).md)
  Creates a new image presentation component to present a spatial 3D image.
### Instance Properties
- [var availableViewingModes: Set<ImagePresentationComponent.ViewingMode>](imagepresentationcomponent/availableviewingmodes.md)
  The currently valid viewing modes for the image being presented.
- [var desiredViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/desiredviewingmode.md)
  The user-selected preferred content viewing mode.
- [var presentationScreenSize: SIMD2<Float>](imagepresentationcomponent/presentationscreensize.md)
  The size of the screen presenting the image, with the format [width, height] in meters.
- [var screenHeight: Float](imagepresentationcomponent/screenheight.md)
  The height of the screen mesh, in meters, when the image is presented in a non-immersive viewing mode.
- [var screenImageDimension: SIMD2<Float>](imagepresentationcomponent/screenimagedimension.md)
  The image resolution of the currently presented image, in pixels.
- [var viewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.property.md)
  The currently active viewing mode of the presented image.
### Instance Methods
- [func aspectRatio(for: ImagePresentationComponent.ViewingMode) -> Float?](imagepresentationcomponent/aspectratio(for:).md)
  The aspect ratio of the image this component will present for the requested viewing mode.
### Type Methods
- [static supportedViewingModes(for:)](imagepresentationcomponent/supportedviewingmodes(for:).md)
  The viewing modes supported by the provided image source.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct HoverEffectComponent](hovereffectcomponent.md)
  A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.
- [struct BillboardComponent](billboardcomponent.md)
  A component that orients an entity instance so that it continuously points toward the active camera.
- [struct EnvironmentBlendingComponent](environmentblendingcomponent.md)
  A component which controls how an entity will blend visually with objects in the user’s local environment
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent)*