# MDLCamera

**Framework**: Model I/O  
**Kind**: class

A point of view for rendering a 3D scene, along with a set of parameters describing an intended appearance for rendering.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLCamera
```

#### Overview

Camera parameters include basic information—such as the [`projectionMatrix`](mdlcamera/projectionmatrix.md) and [`fieldOfView`](mdlcamera/fieldofview.md) properties—for use with any renderer, as well as attributes that model real-world cameras—such as the [`fStop`](mdlcamera/fstop.md) and [`exposure`](mdlcamera/exposure.md) properties—for use in a renderer based on realistic optical physics.

## Topics

### Managing Camera Position and Orientation
- [func frameBoundingBox(MDLAxisAlignedBoundingBox, setNearAndFar: Bool)](mdlcamera/frameboundingbox(_:setnearandfar:).md)
  Moves the camera such that the specified bounding box lies entirely within the camera’s field of view.
- [func look(at: vector_float3)](mdlcamera/look(at:).md)
  Orients the camera to face toward the specified point.
- [func look(at: vector_float3, from: vector_float3)](mdlcamera/look(at:from:).md)
  Sets the camera’s position and orients the camera to face toward the specified point.
### Managing Camera Perspective
- [var projectionMatrix: matrix_float4x4](mdlcamera/projectionmatrix.md)
  A transformation matrix that determines the extent of a scene visible to the camera.
- [var projection: MDLCameraProjection](mdlcamera/projection.md)
  The style of projection transform used by the camera.
- [enum MDLCameraProjection](mdlcameraprojection.md)
  Options for camera projection styles, used by the [`projection`](mdlcamera/projection.md) property.
- [var nearVisibilityDistance: Float](mdlcamera/nearvisibilitydistance.md)
  The camera’s near depth limit.
- [var farVisibilityDistance: Float](mdlcamera/farvisibilitydistance.md)
  The camera’s far depth limit.
- [var fieldOfView: Float](mdlcamera/fieldofview.md)
  The camera’s field of view, in degrees.
- [func ray(to: vector_int2, forViewPort: vector_int2) -> vector_float3](mdlcamera/ray(to:forviewport:).md)
  Returns a point, in 3D world coordinates, corresponding to the specified 2D view coordinates.
- [var worldToMetersConversionScale: Float](mdlcamera/worldtometersconversionscale.md)
  The scale factor to meters from the world coordinate system containing the camera.
### Modeling a Physical Lens
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
- [var shutterOpenInterval: TimeInterval](mdlcamera/shutteropeninterval.md)
  The duration, in seconds, for which the camera’s simulated shutter is open during each frame.
### Modeling a Physical Imaging Surface
- [var sensorVerticalAperture: Float](mdlcamera/sensorverticalaperture.md)
  The height, in millimeters, of the camera’s simulated imaging surface.
- [var sensorAspect: Float](mdlcamera/sensoraspect.md)
  The ratio of width to height for the camera’s simulated imaging surface.
- [var sensorEnlargement: vector_float2](mdlcamera/sensorenlargement.md)
  The horizontal and vertical scale factors that determine the active region of the sensor.
- [var sensorShift: vector_float2](mdlcamera/sensorshift.md)
  The horizontal and vertical offsets, in millimeters, of the center of the camera image relative to the center of the simulated lens.
- [var flash: vector_float3](mdlcamera/flash.md)
  Red, green, and blue factors to be used in brightening darker areas of the camera’s image.
- [var exposure: vector_float3](mdlcamera/exposure.md)
  Red, green, and blue factors that scale each color channel in the camera’s image.
- [var exposureCompression: vector_float2](mdlcamera/exposurecompression.md)
  Two parameters that determine the brightness compression curve for colors in the camera’s image.

## Relationships

### Inherits From
- [MDLObject](mdlobject.md)
### Inherited By
- [MDLStereoscopicCamera](mdlstereoscopiccamera.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLStereoscopicCamera](mdlstereoscopiccamera.md)
  A point of view for rendering a stereoscopic display of a 3D scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera)*