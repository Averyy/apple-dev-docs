# SCNCamera

**Framework**: SceneKit  
**Kind**: class

A set of camera attributes that can be attached to a node to provide a point of view for displaying the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNCamera
```

#### Overview

To display a scene, you must designate a node whose [`camera`](scncamera/camera.md) property contains a camera object as the point of view.

The [`SCNNode`](scnnode.md) object containing a camera defines a point of view—that is, the position and orientation of the camera. A camera’s direction of view is always along the negative z-axis of the node’s local coordinate system. To point the camera at different parts of your scene, use the [`position`](scnnode/position.md), [`rotation`](scnnode/rotation.md), or [`transform`](scnnode/transform.md) property of the node containing it. (Alternatively, to ensure that a camera always points at a particular element of your scene even when that element moves, attach a [`SCNLookAtConstraint`](scnlookatconstraint.md) object to the node containing the camera.)

An [`SCNCamera`](scncamera.md) object itself defines the shape and, in part, the appearance of the rendered scene as seen from its point of view. By default, a camera defines a perspective projection, whose field of view (FOV) and near and far visibility limits you control using the properties listed in Adjusting Camera Perspective and illustrated below.

![None](https://docs-assets.developer.apple.com/published/95a05c81bd3d55307b809c94ef53c2c4/media-2929769%402x.png)

## Topics

### Managing Camera Attributes
- [var name: String?](scncamera/name.md)
  A name associated with the camera object.
### Adjusting Camera Perspective
- [var zNear: Double](scncamera/znear.md)
  The camera’s near depth limit. Animatable.
- [var zFar: Double](scncamera/zfar.md)
  The camera’s far depth limit. Animatable.
- [var automaticallyAdjustsZRange: Bool](scncamera/automaticallyadjustszrange.md)
  A Boolean value that determines whether the camera automatically adjusts its [`zNear`](scncamera/znear.md) and [`zFar`](scncamera/zfar.md) depth limits.
### Managing Field of View
- [var fieldOfView: CGFloat](scncamera/fieldofview.md)
  The vertical or horizontal viewing angle of the camera.
- [var focalLength: CGFloat](scncamera/focallength.md)
  The camera’s focal length, in millimeters.
- [var sensorHeight: CGFloat](scncamera/sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](scncamera/projectiondirection.md)
  The axis used to determine field of view or orthographic scale.
- [enum SCNCameraProjectionDirection](scncameraprojectiondirection.md)
  Options for the axis used to determine field of view or orthographic projection.
### Managing the Projection Transform
- [var projectionTransform: SCNMatrix4](scncamera/projectiontransform.md)
  The camera’s projection transformation.
- [var usesOrthographicProjection: Bool](scncamera/usesorthographicprojection.md)
  A Boolean value that determines whether the camera uses an orthographic projection.
- [var orthographicScale: Double](scncamera/orthographicscale.md)
  Specifies the camera’s magnification factor when using an orthographic projection.
### Choosing Nodes to Be Visible to the Camera
- [var categoryBitMask: Int](scncamera/categorybitmask.md)
  A mask that defines which categories this camera belongs to.
### Adding Depth-of-Field Effects
- [var wantsDepthOfField: Bool](scncamera/wantsdepthoffield.md)
  A Boolean value that determines whether SceneKit renders depth-of-field blur effects for the camera.
- [var focusDistance: CGFloat](scncamera/focusdistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var fStop: CGFloat](scncamera/fstop.md)
  The physical camera aperture simulated by SceneKit for depth-of-field effects. Animatable.
- [var apertureBladeCount: Int](scncamera/aperturebladecount.md)
  The number of physical camera aperture blades simulated by SceneKit for depth-of-field effects.
- [var focalBlurSampleCount: Int](scncamera/focalblursamplecount.md)
  The number of pixel samples SceneKit uses to create depth-of-field blur effects.
### Adding Motion Blur Effects
- [var motionBlurIntensity: CGFloat](scncamera/motionblurintensity.md)
  A factor that determines the intensity of motion blur effects. Animatable.
### Adding High Dynamic Range Effects
- [var wantsHDR: Bool](scncamera/wantshdr.md)
  A Boolean value that determines whether SceneKit applies High Dynamic Range (HDR) postprocessing effects to a scene.
- [var exposureOffset: CGFloat](scncamera/exposureoffset.md)
  A logarithmic bias that adjusts the results of SceneKit’s tone mapping operation, brightening or darkening the visible scene.
- [var averageGray: CGFloat](scncamera/averagegray.md)
  The luminance level to use as the midpoint of a tone mapping curve.
- [var whitePoint: CGFloat](scncamera/whitepoint.md)
  The luminance level to use as the upper end of a tone mapping curve.
- [var minimumExposure: CGFloat](scncamera/minimumexposure.md)
  The minimum exposure value to use in tone mapping.
- [var maximumExposure: CGFloat](scncamera/maximumexposure.md)
  The minimum exposure value to use in tone mapping.
### Adding Automatic HDR Exposure Adaptation
- [var wantsExposureAdaptation: Bool](scncamera/wantsexposureadaptation.md)
  A Boolean value that determines whether SceneKit automatically adjusts the exposure level.
- [var exposureAdaptationBrighteningSpeedFactor: CGFloat](scncamera/exposureadaptationbrighteningspeedfactor.md)
  The relative duration of automatically animated exposure transitions from dark to bright areas.
- [var exposureAdaptationDarkeningSpeedFactor: CGFloat](scncamera/exposureadaptationdarkeningspeedfactor.md)
  The relative duration of automatically animated exposure transitions from bright to dark areas.
### Adjusting Rendered Colors
- [var contrast: CGFloat](scncamera/contrast.md)
  An adjustment factor to apply to the overall visual contrast of the rendered scene.
- [var saturation: CGFloat](scncamera/saturation.md)
  An adjustment factor to apply to the overall color saturation of the rendered scene.
- [var colorGrading: SCNMaterialProperty](scncamera/colorgrading.md)
  A texture for applying color grading effects to the entire rendered scene.
### Adding Stylistic Visual Effects
- [var bloomIntensity: CGFloat](scncamera/bloomintensity.md)
  The magnitude of bloom effect to apply to highlights in the rendered scene. Animatable.
- [var bloomThreshold: CGFloat](scncamera/bloomthreshold.md)
  The brightness threshold at which to apply a bloom effect to highlights in the rendered scene. Animatable.
- [var bloomBlurRadius: CGFloat](scncamera/bloomblurradius.md)
  The radius, in pixels, for the blurring portion of the bloom effect applied to highlights in the rendered scene. Animatable.
- [var colorFringeIntensity: CGFloat](scncamera/colorfringeintensity.md)
  The blend factor for fading the color fringing effect applied to the rendered scene.
- [var colorFringeStrength: CGFloat](scncamera/colorfringestrength.md)
  The magnitude of color fringing effect to apply to the rendered scene.
- [var vignettingIntensity: CGFloat](scncamera/vignettingintensity.md)
  The magnitude of vignette (darkening around edges) effect to apply to the rendered scene.
- [var vignettingPower: CGFloat](scncamera/vignettingpower.md)
  The amount of the rendered scene to darken with a vignette effect.
### Adding Screen-Space Ambient Occlusion
- [var screenSpaceAmbientOcclusionIntensity: CGFloat](scncamera/screenspaceambientocclusionintensity.md)
  The intensity of the screen-space ambient occlusion effect applied in camera rendering.
- [var screenSpaceAmbientOcclusionRadius: CGFloat](scncamera/screenspaceambientocclusionradius.md)
  The distance, in units of scene space, at which ambient occlusion takes effect.
- [var screenSpaceAmbientOcclusionBias: CGFloat](scncamera/screenspaceambientocclusionbias.md)
  An offset for modulating ambient occlusion effects.
- [var screenSpaceAmbientOcclusionDepthThreshold: CGFloat](scncamera/screenspaceambientocclusiondepththreshold.md)
  The maximum depth difference, in units of scene space, at which to apply ambient occlusion effects.
- [var screenSpaceAmbientOcclusionNormalThreshold: CGFloat](scncamera/screenspaceambientocclusionnormalthreshold.md)
  The magnitude of the blur effect applied to create ambient occlusion shadows.
### Deprecated
- [var yFov: Double](scncamera/yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var xFov: Double](scncamera/xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalDistance: CGFloat](scncamera/focaldistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var focalSize: CGFloat](scncamera/focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](scncamera/focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.
- [var aperture: CGFloat](scncamera/aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.
### Instance Properties
- [var bloomIterationCount: Int](scncamera/bloomiterationcount.md)
- [var bloomIterationSpread: CGFloat](scncamera/bloomiterationspread.md)
- [var grainIntensity: CGFloat](scncamera/grainintensity.md)
- [var grainIsColored: Bool](scncamera/grainiscolored.md)
- [var grainScale: CGFloat](scncamera/grainscale.md)
- [var whiteBalanceTemperature: CGFloat](scncamera/whitebalancetemperature.md)
- [var whiteBalanceTint: CGFloat](scncamera/whitebalancetint.md)
### Instance Methods
- [func projectionTransform(withViewportSize: CGSize) -> SCNMatrix4](scncamera/projectiontransform(withviewportsize:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)
- [SCNTechniqueSupport](scntechniquesupport.md)

## See Also

- [class SCNLight](scnlight.md)
  A light source that can be attached to a node to illuminate the scene.
- [class SCNMaterial](scnmaterial.md)
  A set of shading attributes that define the appearance of a geometry’s surface when rendered.
- [class SCNMaterialProperty](scnmaterialproperty.md)
  A container for the color or texture of one of a material’s visual properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera)*