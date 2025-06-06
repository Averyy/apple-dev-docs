# bokehKernel(withSize:)

**Framework**: Model I/O  
**Kind**: method

Creates and returns a texture, based on the camera’s aperture blade count, to be used in rendering out-of-focus highlights in a scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func bokehKernel(withSize size: vector_int2) -> MDLTexture
```

#### Return Value

A new bokeh kernel texture.

#### Discussion

The shape of a real-world camera’s aperture is determined by the number of overlapping blades that form an adjustable iris, whose center opening light passes through between the lens and the imaging surface (film or sensor). This shape affects that of out-of-focus highlights, commonly called , that appear in images seen by the camera. The aesthetic quality of a lens’ bokeh is one of the characteristics that drives the choice of a lens for a particular scene. To specify the blade count for a camera, use the [`apertureBladeCount`](mdlcamera/aperturebladecount.md) property. Then, use this method to create a texture image for use in rendering bokeh highlights.

A renderer typically uses this texture to simulate lens effects in one of two ways:

- As the kernel for a convolution filter over the entire rendered image. This option provides a realistic, but computationally expensive blur effect for out-of-focus areas.
- As a sprite texture placed at the locations of point highlights in the rendered scene. This option can produce a facsimile of realistic bokeh effects at a lower cost to rendering performance.

## Parameters

- `size`: The pixel dimensions of the texture to create.

## See Also

- [var barrelDistortion: Float](mdlcamera/barreldistortion.md)
  The first coefficient for determining the radial distortion applied to pixels rendered using the camera.
- [var fisheyeDistortion: Float](mdlcamera/fisheyedistortion.md)
  The second coefficient for determining the radial distortion applied to pixels rendered using the camera.
- [var opticalVignetting: Float](mdlcamera/opticalvignetting.md)
  The amount of radial light attenuation around the edges of an image rendered using the camera.
- [var chromaticAberration: Float](mdlcamera/chromaticaberration.md)
  The amount of radial color shift around the edges of an image rendered using the camera.
- [var focalLength: Float](mdlcamera/focallength.md)
  The focal length, in millimeters, of the camera’s simulated lens.
- [var fStop: Float](mdlcamera/fstop.md)
  The relative aperture ratio of the camera’s simulated lens.
- [var apertureBladeCount: Int](mdlcamera/aperturebladecount.md)
  The number of blades in the camera’s simulated aperture.
- [var maximumCircleOfConfusion: Float](mdlcamera/maximumcircleofconfusion.md)
  The maximum diameter, in millimeters on the imaging plane, at which light from a point source should appear in an image rendered using the camera.
- [var focusDistance: Float](mdlcamera/focusdistance.md)
  The distance, in meters, at which the lens is focused.
- [var shutterOpenInterval: TimeInterval](mdlcamera/shutteropeninterval.md)
  The duration, in seconds, for which the camera’s simulated shutter is open during each frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/bokehkernel(withsize:))*