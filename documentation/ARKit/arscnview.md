# ARSCNView

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

A view that blends virtual 3D content from SceneKit into your augmented reality experience.

**Availability**:
- iOS 11.0+ - Deprecated in 26.0
- iPadOS 11.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- visionOS

> **Deprecated**: Use [`RealityView`](../RealityKit/realityview.md) instead.

## Declaration

```swift
class ARSCNView
```

```objc
@interface ARSCNView : SCNView
```

#### Overview

> ❗ **Important**: SceneKit is deprecated, use [RealityKit](../RealityKit/RealityKit.md) instead. For more information, see WWDC25 session 288: [Bring your SceneKit projects to RealityKit](https://developer.apple.com/videos/play/wwdc2025/288/).

The [`ARSCNView`](./arscnview.md) class provides an easy way to create augmented reality experiences that blend virtual 3D content with a device camera view of the real world. When you run the view’s provided [`ARSession`](./arsession.md) object:

- The view automatically renders the live video feed from the device camera as the scene background.
- The world coordinate system of the view’s SceneKit scene directly responds to the AR world coordinate system established by the session configuration.
- The view automatically moves its SceneKit camera to match the real-world movement of the device.

ARKit automatically matches SceneKit’s coordinate space to the real world, so after you place your app’s virtual content, it maintains the illusion of resting in the real-world as the user moves the device. See [Providing 3D Virtual Content with SceneKit](./providing-3d-virtual-content-with-scenekit.md).

You don’t necessarily need to use the [`ARAnchor`](./aranchor.md) class to track positions of objects you add to the scene, but by implementing [`ARSCNViewDelegate`](./arscnviewdelegate.md) methods, you can add SceneKit content to any anchors that are automatically detected by ARKit.

Because ARKit requires Metal, use only Metal features of SceneKit. For example:

- This class supports only [`SCNProgram`](../SceneKit/scnprogram.md) instances with Metal Shading Language code.
- If you set the [`preferredRenderingAPI`](../SceneKit/scnview/option/preferredrenderingapi.md) property to [`SCNRenderingAPI.openGLES2`](../SceneKit/scnrenderingapi/opengles2.md), the framework reverts the value to  [`SCNRenderingAPI.metal`](../SceneKit/scnrenderingapi/metal.md).

## Topics

### Essentials
- [Providing 3D Virtual Content with SceneKit](./providing-3d-virtual-content-with-scenekit.md)
  Use SceneKit to add realistic three-dimensional objects to your AR experience.
- [var session: ARSession](./arscnview/session.md)
  The AR session that manages motion tracking and camera image processing for the view’s contents.
- [var scene: SCNScene](./arscnview/scene.md)
  The SceneKit scene to be displayed in the view.
### Responding to AR Updates
- [var delegate: (any ARSCNViewDelegate)?](./arscnview/delegate.md)
  An object you provide to mediate synchronization of the view’s AR scene information with SceneKit content.
- [protocol ARSCNViewDelegate](./arscnviewdelegate.md)
  Methods you can implement to mediate the automatic synchronization of SceneKit content with an AR session.
### Finding Real-World Surfaces
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](./arscnview/hittest%28_,types%29.md)
  Searches for real-world objects or AR anchors in the captured camera image corresponding to a point in the SceneKit view.
- [func raycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?](./arscnview/raycastquery%28from,allowing,alignment%29.md)
  Creates a raycast query that originates from a point on the view, aligned with the center of the camera’s field of view.
### Mapping Content to Real-World Positions
- [func anchor(for: SCNNode) -> ARAnchor?](./arscnview/anchor%28for%29.md)
  Returns the AR anchor associated with the specified SceneKit node, if any.
- [func node(for: ARAnchor) -> SCNNode?](./arscnview/node%28for%29.md)
  Returns the SceneKit node associated with the specified AR anchor, if any.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4) -> simd_float3?](./arscnview/unprojectpoint%28_,ontoplane%29.md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.
- [- unprojectPoint:ontoPlaneWithTransform:](./arscnview/unprojectpoint_ontoplanewithtransform_.md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.
### Managing Lighting
- [var automaticallyUpdatesLighting: Bool](./arscnview/automaticallyupdateslighting.md)
  A Boolean value that specifies whether ARKit creates and updates SceneKit lights in the view’s scene.
### Debugging AR Display
- [typealias ARSCNDebugOptions](./arscndebugoptions.md)
  Options for drawing overlay content to aid debugging of AR tracking in a SceneKit view.
### Managing Rendering Effects
- [var rendersMotionBlur: Bool](./arscnview/rendersmotionblur.md)
  Determines whether the view renders motion blur.
- [var rendersCameraGrain: Bool](./arscnview/renderscameragrain.md)
  A flag that determines whether SceneKit applies image noise characteristics to your app’s virtual content.

## Relationships

### Inherits From
- [SCNView](../SceneKit/scnview.md)
### Conforms To
- [ARSessionProviding](./arsessionproviding.md)
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [SCNSceneRenderer](../SceneKit/scnscenerenderer.md)
- [SCNTechniqueSupport](../SceneKit/scntechniquesupport.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Views
- [struct RealityView](../RealityKit/realityview.md)
  A view that contains RealityKit content.
- [class ARView](../RealityKit/arview.md)
  A view that enables you to display an AR experience with RealityKit.
- [class ARSKView](./arskview.md)
  A view that blends virtual 2D content from SpriteKit into the 3D space of an augmented reality experience.
- [class ARCoachingOverlayView](./arcoachingoverlayview.md)
  A view that displays standardized onboarding instructions to direct users toward a specific goal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview)*