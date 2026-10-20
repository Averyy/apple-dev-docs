# ImagePresentationComponent.Spatial3DImage

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A 3D spatial scene created from a 2D image.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
class Spatial3DImage
```

#### Overview

Create and generate a `Spatial3DImage`  to present a *spatial scene* in RealityKit. Spatial scenes are a 3D representation of a 2D image or photo which RealityKit renders with depth and motion parallax.

##### Spatial scene generation

To present a `Spatial3DImage` as a spatial scene, you must first *generate* it. Call the [`generate()`](./spatial3dimage/generate%28%29.md) method to generate an in-memory representation of a spatial scene from the original image. Generation can take a few seconds to complete.

> **Note**: You can’t generate a `Spatial3DImage` with the visionOS Simulator. You can create and work with `Spatial3DImage` instances in the Simulator, but calling the [`generate()`](./spatial3dimage/generate%28%29.md) method throws an error.

You can choose to pre-generate a spatial scene in advance of presentation, or post-generate it in response to an interaction such as someone pressing a button.

In either case, start by creating a new `Spatial3DImage` from a local file URL for an existing image, or from an existing `CGImageSource`.

To pre-generate and present the image as a spatial scene, call the [`generate()`](./spatial3dimage/generate%28%29.md) method on the `Spatial3DImage` to generate its in-memory spatial scene representation. Next, use the [`init(spatial3DImage:)`](./init%28spatial3dimage%29.md) initializer to create an [`ImagePresentationComponent`](../imagepresentationcomponent.md) from the generated `Spatial3DImage`. Set the component’s [`desiredViewingMode`](./desiredviewingmode.md) to [`spatial3D`](./viewingmode-swift.struct/spatial3d.md) or [`spatial3DImmersive`](./viewingmode-swift.struct/spatial3dimmersive.md), then add the component to an entity to present the spatial scene immediately.

To post-generate a spatial scene, create a new [`ImagePresentationComponent`](../imagepresentationcomponent.md) from the `Spatial3DImage` *before* generating it, and add the component to an entity. By default, the component displays the image with a monoscopic ([`mono`](./viewingmode-swift.struct/mono.md)) viewing mode. If you created the image from a spatial photo, you can choose to present the `Spatial3DImage` as a spatial photo instead by setting the component’s [`desiredViewingMode`](./desiredviewingmode.md) to [`spatialStereo`](./viewingmode-swift.struct/spatialstereo.md) or [`spatialStereoImmersive`](./viewingmode-swift.struct/spatialstereoimmersive.md).

In your app’s UI, add a button or other trigger to convert the image to 3D. When someone presses the button, set the component’s [`desiredViewingMode`](./desiredviewingmode.md) to [`spatial3D`](./viewingmode-swift.struct/spatial3d.md) or [`spatial3DImmersive`](./viewingmode-swift.struct/spatial3dimmersive.md), to indicate that you want the component to present the spatial scene as soon as the app finishes generating it. Then, call the [`generate()`](./spatial3dimage/generate%28%29.md) method to begin the generation process. The component displays a generation animation, similar to the Photos app on visionOS, and transitions to presenting the spatial scene as soon as generation completes.

> **Note**: Spatial scenes are created by an AI algorithm that leverages computational depth to create multiple perspectives of a 2D photo. In some cases, spatial scenes may contain visual artifacts. When you include a spatial scene in your app’s UI, consider providing a button to switch to the original 2D photo instead, by setting the component’s [`desiredViewingMode`](./desiredviewingmode.md) to [`mono`](./viewingmode-swift.struct/mono.md).

## Topics

### Creating a spatial scene from a 2D image or spatial photo
- [convenience init(contentsOf: URL) async throws](./spatial3dimage/init%28contentsof%29.md)
  Initializes a spatial 3D image from the contents of an image file.
- [init(imageSource: CGImageSource) async throws](./spatial3dimage/init%28imagesource%29.md)
  Initializes a spatial 3D image from the contents of an image source.
### Generating a spatial scene
- [func generate() async throws](./spatial3dimage/generate%28%29.md)
  Creates a 3D representation of the image if one does not already exist.

## See Also

### Images and spatial scenes
- [struct ImagePresentationComponent](../imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/spatial3dimage)*