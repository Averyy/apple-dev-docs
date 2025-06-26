# ImagePresentationComponent.Spatial3DImage

**Framework**: RealityKit  
**Kind**: class

A 3D spatial scene created from a 2D image.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
class Spatial3DImage
```

#### Overview

Create and generate a `Spatial3DImage`  to present a  in RealityKit. Spatial scenes are a 3D representation of a 2D image or photo which RealityKit renders with depth and motion parallax.

##### Spatial Scene Generation

To present a `Spatial3DImage` as a spatial scene, you must first  it. Call the [`generate()`](imagepresentationcomponent/spatial3dimage/generate().md) method to generate an in-memory representation of a spatial scene from the original image. Generation can take a few seconds to complete.

> **Note**: You can’t generate a `Spatial3DImage` with the visionOS Simulator. You can create and work with `Spatial3DImage` instances in the Simulator, but calling the [`generate()`](imagepresentationcomponent/spatial3dimage/generate().md) method throws an error.

You can choose to pre-generate a spatial scene in advance of presentation, or post-generate it in response to an interaction such as somene pressing a button.

In either case, start by creating a new `Spatial3DImage` from a local file URL for an existing image, or from an existing `CGImageSource`.

To pre-generate and present the image as a spatial scene, call the [`generate()`](imagepresentationcomponent/spatial3dimage/generate().md) method on the `Spatial3DImage` to generate its in-memory spatial scene representation. Next, use the [`init(spatial3DImage:)`](imagepresentationcomponent/init(spatial3dimage:).md) initializer to create an [`ImagePresentationComponent`](imagepresentationcomponent.md) from the generated `Spatial3DImage`. Set the component’s [`desiredViewingMode`](imagepresentationcomponent/desiredviewingmode.md) to [`spatial3D`](imagepresentationcomponent/viewingmode-swift.struct/spatial3d.md) or [`spatial3DImmersive`](imagepresentationcomponent/viewingmode-swift.struct/spatial3dimmersive.md), then add the component to an entity to present the spatial scene immediately.

To post-generate a spatial scene, create a new [`ImagePresentationComponent`](imagepresentationcomponent.md) from the `Spatial3DImage`  generating it, and add the component to an entity. By default, the component displays the image with a monoscopic ([`mono`](imagepresentationcomponent/viewingmode-swift.struct/mono.md)) viewing mode. If you created the image from a spatial photo, you can choose to present the `Spatial3DImage` as a spatial photo instead by setting the component’s [`desiredViewingMode`](imagepresentationcomponent/desiredviewingmode.md) to [`spatialStereo`](imagepresentationcomponent/viewingmode-swift.struct/spatialstereo.md) or [`spatialStereoImmersive`](imagepresentationcomponent/viewingmode-swift.struct/spatialstereoimmersive.md).

In your app’s UI, add a button or other trigger to convert the image to 3D. When someone presses the button, set the component’s [`desiredViewingMode`](imagepresentationcomponent/desiredviewingmode.md) to [`spatial3D`](imagepresentationcomponent/viewingmode-swift.struct/spatial3d.md) or [`spatial3DImmersive`](imagepresentationcomponent/viewingmode-swift.struct/spatial3dimmersive.md), to indicate that you want the component to present the spatial scene as soon as the app finishes generating it. Then, call the [`generate()`](imagepresentationcomponent/spatial3dimage/generate().md) method to begin the generation process. The component displays a generation animation, similar to the Photos app on visionOS, and transitions to presenting the spatial scene as soon as generation completes.

## Topics

### Creating a spatial scene from a 2D image or spatial photo
- [convenience init(contentsOf: URL) async throws](imagepresentationcomponent/spatial3dimage/init(contentsof:).md)
  Initializes a spatial 3D image from the contents of an image file.
- [init(imageSource: CGImageSource) async throws](imagepresentationcomponent/spatial3dimage/init(imagesource:).md)
  Initializes a spatial 3D image from the contents of an image source.
### Generating a spatial scene
- [func generate() async throws](imagepresentationcomponent/spatial3dimage/generate.md)
  Creates a 3D representation of the image if one does not already exist.

## See Also

- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/spatial3dimage)*