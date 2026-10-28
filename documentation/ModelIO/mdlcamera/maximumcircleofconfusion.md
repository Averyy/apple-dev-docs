# maximumCircleOfConfusion

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The maximum diameter, in millimeters on the imaging plane, at which light from a point source should appear in an image rendered using the camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maximumCircleOfConfusion: Float { get set }
```

```objc
@property (nonatomic, assign) float maximumCircleOfConfusion;
```

## Discussion

In a physically based camera simulation, the size of out-of-focus highlights that appear in images seen by the camera—commonly called *bokeh*—is a function of other camera properties, such as focal length, pupil aperture, sensor size, and distance to the subject. However, it can be useful for aesthetic reasons to limit the size of such highlights.

The default maximum circle of confusion is 0.05 mm.

## See Also

### Modeling a Physical Lens
- [var barrelDistortion: Float](./barreldistortion.md)
  The first coefficient for determining the radial distortion applied to pixels rendered using the camera.
- [var fisheyeDistortion: Float](./fisheyedistortion.md)
  The second coefficient for determining the radial distortion applied to pixels rendered using the camera.
- [var opticalVignetting: Float](./opticalvignetting.md)
  The amount of radial light attenuation around the edges of an image rendered using the camera.
- [var chromaticAberration: Float](./chromaticaberration.md)
  The amount of radial color shift around the edges of an image rendered using the camera.
- [var focalLength: Float](./focallength.md)
  The focal length, in millimeters, of the camera’s simulated lens.
- [var fStop: Float](./fstop.md)
  The relative aperture ratio of the camera’s simulated lens.
- [var apertureBladeCount: Int](./aperturebladecount.md)
  The number of blades in the camera’s simulated aperture.
- [func bokehKernel(withSize: vector_int2) -> MDLTexture](./bokehkernel%28withsize%29.md)
  Creates and returns a texture, based on the camera’s aperture blade count, to be used in rendering out-of-focus highlights in a scene.
- [var focusDistance: Float](./focusdistance.md)
  The distance, in meters, at which the lens is focused.
- [var shutterOpenInterval: TimeInterval](./shutteropeninterval.md)
  The duration, in seconds, for which the camera’s simulated shutter is open during each frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/maximumcircleofconfusion)*