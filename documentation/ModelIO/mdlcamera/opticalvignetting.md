# opticalVignetting

**Framework**: Model I/O  
**Kind**: property

The amount of radial light attenuation around the edges of an image rendered using the camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var opticalVignetting: Float { get set }
```

#### Discussion

Optical vignetting occurs to some degree in all lenses. It results from light at the edge of an image being blocked as it travels past the lens hood and the internal lens apertures. It is more prevalent with wide apertures. A value of `0.0` (the default) indicates no optical vignetting, and a value of `1.0` indicates that vignetting affects all locations in the image according to radial distance. Optical vignetting also occurs in head-mounted displays, and the value here can be used as an intended amount of vignetting to apply to an image.

## See Also

- [var barrelDistortion: Float](mdlcamera/barreldistortion.md)
  The first coefficient for determining the radial distortion applied to pixels rendered using the camera.
- [var fisheyeDistortion: Float](mdlcamera/fisheyedistortion.md)
  The second coefficient for determining the radial distortion applied to pixels rendered using the camera.
- [var chromaticAberration: Float](mdlcamera/chromaticaberration.md)
  The amount of radial color shift around the edges of an image rendered using the camera.
- [var focalLength: Float](mdlcamera/focallength.md)
  The focal length, in millimeters, of the camera’s simulated lens.
- [var fStop: Float](mdlcamera/fstop.md)
  The relative aperture ratio of the camera’s simulated lens.
- [var apertureBladeCount: Int](mdlcamera/aperturebladecount.md)
  The number of blades in the camera’s simulated aperture.
- [func bokehKernel(withSize: vector_int2) -> MDLTexture](mdlcamera/bokehkernel(withsize:).md)
  Creates and returns a texture, based on the camera’s aperture blade count, to be used in rendering out-of-focus highlights in a scene.
- [var maximumCircleOfConfusion: Float](mdlcamera/maximumcircleofconfusion.md)
  The maximum diameter, in millimeters on the imaging plane, at which light from a point source should appear in an image rendered using the camera.
- [var focusDistance: Float](mdlcamera/focusdistance.md)
  The distance, in meters, at which the lens is focused.
- [var shutterOpenInterval: TimeInterval](mdlcamera/shutteropeninterval.md)
  The duration, in seconds, for which the camera’s simulated shutter is open during each frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/opticalvignetting)*