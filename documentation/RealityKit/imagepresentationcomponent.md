# ImagePresentationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that supports general image presentation.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct ImagePresentationComponent
```

#### Overview

`ImagePresentationComponent` supports the presentation of three different kinds of images in RealityKit:

- A traditional 2D image.
- A , which is a stereoscopic photo with additional spatial metadata, as captured on iPhone 15 Pro or later and Apple Vision Pro.
- A , which is a 3D image generated from an existing 2D image or photo.

To present a 2D image or a spatial photo, create a new `ImagePresentationComponent` from a local file URL for the existing image, or from an existing `CGImageSource`.

To generate and present a spatial scene from an existing image, create a [`ImagePresentationComponent.Spatial3DImage`](imagepresentationcomponent/spatial3dimage.md) from the image; call the [`generate()`](imagepresentationcomponent/spatial3dimage/generate().md) method on your new spatial 3D image; then create a new `ImagePresentationComponent` with [`init(spatial3DImage:)`](imagepresentationcomponent/init(spatial3dimage:).md).

##### Viewing Modes

By default, an `ImagePresentationComponent` presents its image in a [`mono`](imagepresentationcomponent/viewingmode-swift.struct/mono.md) viewing mode, regardless of what kind of image you create it with.

To request a different viewing mode, set the component’s [`desiredViewingMode`](imagepresentationcomponent/desiredviewingmode.md) property, and add the component to an entity with the updated value.

To discover which viewing modes a component’s image supports, query the component’s [`availableViewingModes`](imagepresentationcomponent/availableviewingmodes.md) property. The [`availableViewingModes`](imagepresentationcomponent/availableviewingmodes.md) set always contains [`mono`](imagepresentationcomponent/viewingmode-swift.struct/mono.md) as an option.

When you create this component with a valid spatial photo, the set of available viewing modes also contains [`spatialStereo`](imagepresentationcomponent/viewingmode-swift.struct/spatialstereo.md) and [`spatialStereoImmersive`](imagepresentationcomponent/viewingmode-swift.struct/spatialstereoimmersive.md).

If you created the component with a [`ImagePresentationComponent.Spatial3DImage`](imagepresentationcomponent/spatial3dimage.md), and have called the [`generate()`](imagepresentationcomponent/spatial3dimage/generate().md) method to generate it, the set of available viewing modes will also contain [`spatial3D`](imagepresentationcomponent/viewingmode-swift.struct/spatial3d.md) and [`spatial3DImmersive`](imagepresentationcomponent/viewingmode-swift.struct/spatial3dimmersive.md).

> **Note**: The component may not present the image with the [`desiredViewingMode`](imagepresentationcomponent/desiredviewingmode.md) you choose. Query [`viewingMode`](imagepresentationcomponent/viewingmode-swift.property.md) to check what viewing mode the component is using.

## Topics

### Creating a component from a 2D image or spatial photo
- [init(contentsOf: URL) async throws](imagepresentationcomponent/init(contentsof:).md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image file URL.
- [init(imageSource: CGImageSource) async throws](imagepresentationcomponent/init(imagesource:).md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image source.
### Creating a component from a spatial scene
- [ImagePresentationComponent.Spatial3DImage](imagepresentationcomponent/spatial3dimage.md)
  A 3D spatial scene created from a 2D image.
- [init(spatial3DImage: ImagePresentationComponent.Spatial3DImage)](imagepresentationcomponent/init(spatial3dimage:).md)
  Creates a new image presentation component to present a spatial 3D image.
### Setting and discovering viewing modes
- [ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.struct.md)
  Image content’s rendering mode.
- [var viewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/viewingmode-swift.property.md)
  The currently active viewing mode of the presented image.
- [var desiredViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationcomponent/desiredviewingmode.md)
  The user-selected preferred content viewing mode.
- [var availableViewingModes: Set<ImagePresentationComponent.ViewingMode>](imagepresentationcomponent/availableviewingmodes.md)
  The currently valid viewing modes for the image being presented.
- [static func supportedViewingModes(for: CGImageSource) -> Set<ImagePresentationComponent.ViewingMode>](imagepresentationcomponent/supportedviewingmodes(for:)-7za1y.md)
  The viewing modes supported by the provided image source.
### Retrieving the current image size
- [func aspectRatio(for: ImagePresentationComponent.ViewingMode) -> Float?](imagepresentationcomponent/aspectratio(for:).md)
  The aspect ratio of the image this component will present for the requested viewing mode.
- [var screenImageDimension: SIMD2<Float>](imagepresentationcomponent/screenimagedimension.md)
  The image resolution of the currently presented image, in pixels.
### Retrieving the current screen mesh size
- [var screenHeight: Float](imagepresentationcomponent/screenheight.md)
  The height of the screen mesh, in meters, when the image is presented in a non-immersive viewing mode.
- [var presentationScreenSize: SIMD2<Float>](imagepresentationcomponent/presentationscreensize.md)
  The size of the screen presenting the image, with the format [width, height] in meters.
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
  A component that controls how an entity blends visually with objects in the local environment.
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent)*