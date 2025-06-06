# ARSCNView

**Framework**: ARKit  
**Kind**: class

A view that blends virtual 3D content from SceneKit into your augmented reality experience.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class ARSCNView
```

#### Overview

The [`ARSCNView`](arscnview.md) class provides the easiest way to create augmented reality experiences that blend virtual 3D content with a device camera view of the real world. When you run the view’s provided [`ARSession`](arsession.md) object:

- The view automatically renders the live video feed from the device camera as the scene background.
- The world coordinate system of the view’s SceneKit scene directly responds to the AR world coordinate system established by the session configuration.
- The view automatically moves its SceneKit camera to match the real-world movement of the device.

ARKit automatically matches SceneKit’s coordinate space to the real world, so after you place your app’s virtual content, it maintains the illusion of resting in the real-world as the user moves the device. See [`Providing 3D Virtual Content with SceneKit`](providing-3d-virtual-content-with-scenekit.md).

You don’t necessarily need to use the [`ARAnchor`](aranchor.md) class to track positions of objects you add to the scene, but by implementing [`ARSCNViewDelegate`](arscnviewdelegate.md) methods, you can add SceneKit content to any anchors that are automatically detected by ARKit.

Because ARKit requires Metal, use only Metal features of SceneKit. For example:

- This class supports only [`SCNProgram`](https://developer.apple.com/documentation/SceneKit/SCNProgram) instances with Metal Shading Language code.
- If you set the [`preferredRenderingAPI`](https://developer.apple.com/documentation/SceneKit/SCNView/Option/preferredRenderingAPI) property to [`SCNRenderingAPI.openGLES2`](https://developer.apple.com/documentation/SceneKit/SCNRenderingAPI/openGLES2), the framework reverts the value to  [`SCNRenderingAPI.metal`](https://developer.apple.com/documentation/SceneKit/SCNRenderingAPI/metal).

## Topics

### Essentials
- [Providing 3D Virtual Content with SceneKit](providing-3d-virtual-content-with-scenekit.md)
  Use SceneKit to add realistic three-dimensional objects to your AR experience.
- [var session: ARSession](arscnview/session.md)
  The AR session that manages motion tracking and camera image processing for the view’s contents.
- [var scene: SCNScene](arscnview/scene.md)
  The SceneKit scene to be displayed in the view.
### Responding to AR Updates
- [var delegate: (any ARSCNViewDelegate)?](arscnview/delegate.md)
  An object you provide to mediate synchronization of the view’s AR scene information with SceneKit content.
- [protocol ARSCNViewDelegate](arscnviewdelegate.md)
  Methods you can implement to mediate the automatic synchronization of SceneKit content with an AR session.
### Finding Real-World Surfaces
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arscnview/hittest(_:types:).md)
  Searches for real-world objects or AR anchors in the captured camera image corresponding to a point in the SceneKit view.
- [func raycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?](arscnview/raycastquery(from:allowing:alignment:).md)
  Creates a raycast query that originates from a point on the view, aligned with the center of the camera’s field of view.
### Mapping Content to Real-World Positions
- [func anchor(for: SCNNode) -> ARAnchor?](arscnview/anchor(for:).md)
  Returns the AR anchor associated with the specified SceneKit node, if any.
- [func node(for: ARAnchor) -> SCNNode?](arscnview/node(for:).md)
  Returns the SceneKit node associated with the specified AR anchor, if any.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4) -> simd_float3?](arscnview/unprojectpoint(_:ontoplane:).md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.
### Managing Lighting
- [var automaticallyUpdatesLighting: Bool](arscnview/automaticallyupdateslighting.md)
  A Boolean value that specifies whether ARKit creates and updates SceneKit lights in the view’s scene.
### Debugging AR Display
- [typealias ARSCNDebugOptions](arscndebugoptions.md)
  Options for drawing overlay content to aid debugging of AR tracking in a SceneKit view.
### Managing Rendering Effects
- [var rendersMotionBlur: Bool](arscnview/rendersmotionblur.md)
  Determines whether the view renders motion blur.
- [var rendersCameraGrain: Bool](arscnview/renderscameragrain.md)
  A flag that determines whether SceneKit applies image noise characteristics to your app’s virtual content.

## Relationships

### Inherits From
- [SCNView](../SceneKit/SCNView.md)
### Conforms To
- [ARSessionProviding](arsessionproviding.md)
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [SCNSceneRenderer](../SceneKit/SCNSceneRenderer.md)
- [SCNTechniqueSupport](../SceneKit/SCNTechniqueSupport.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [@MainActor @objc @preconcurrency class ARView](../RealityKit/ARView.md)
  A view that enables you to display an AR experience with RealityKit.
- [class ARSKView](arskview.md)
  A view that blends virtual 2D content from SpriteKit into the 3D space of an augmented reality experience.
- [class ARCoachingOverlayView](arcoachingoverlayview.md)
  A view that displays standardized onboarding instructions to direct users toward a specific goal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview)*