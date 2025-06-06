# shutterOpenInterval

**Framework**: Model I/O  
**Kind**: property

The duration, in seconds, for which the camera’s simulated shutter is open during each frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var shutterOpenInterval: TimeInterval { get set }
```

#### Discussion

In a real-world camera, the shutter speed determines both the amount of light reaching the imaging surface (film or sensor) and the severity of effects such as motion blur. Shutter time is not the same as frame rate—for example, in a cinema camera running at 24 frames per second, the shutter is open for half of each frame’s duration, so the corresponding shutter time is 1/48 second.

Because shutter time is related to visual effects, not other time-based aspects of rendering a scene, a renderer should treat this property as constant even when those other aspects (such as animation frame rate or frame processing time) vary.

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
- [func bokehKernel(withSize: vector_int2) -> MDLTexture](mdlcamera/bokehkernel(withsize:).md)
  Creates and returns a texture, based on the camera’s aperture blade count, to be used in rendering out-of-focus highlights in a scene.
- [var maximumCircleOfConfusion: Float](mdlcamera/maximumcircleofconfusion.md)
  The maximum diameter, in millimeters on the imaging plane, at which light from a point source should appear in an image rendered using the camera.
- [var focusDistance: Float](mdlcamera/focusdistance.md)
  The distance, in meters, at which the lens is focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/shutteropeninterval)*