# ARView

**Framework**: RealityKit  
**Kind**: class

A view that enables you to display an AR experience with RealityKit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@objc @preconcurrency class ARView
```

## Mentions

- [Handling different-sized objects in physics simulations](handling-different-sized-objects-in-physics-simulations.md)
- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)
- [Applying core image filters as a postprocess effect](applying-core-image-filters-as-a-postprocess-effect.md)
- [Using Metal performance shaders to create custom postprocess effects](using-metal-performance-shaders-to-create-custom-postprocess-effects.md)
- [Loading Reality Composer files using generated code](loading-reality-composer-files-using-generated-code.md)
- [Designing scene hierarchies for efficient physics simulation](designing-scene-hierarchies-for-efficient-physics-simulation.md)
- [Taking Control of Scene Anchoring](taking-control-of-scene-anchoring.md)
- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)
- [Selecting an anchor for a Reality Composer scene](selecting-an-anchor-for-a-reality-composer-scene.md)
- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)
- [Loading remote assets in multiplayer apps](loading-remote-assets.md)

#### Overview

Use an [`ARView`](arview.md) instance to display rendered 3D graphics to the user. You typically add a single view to your app’s storyboard, and then provide an outlet for that view in your code. Alternatively, you can create and add a view to your view hierarchy programmatically at runtime, as you would any other view.

A view has a single [`Scene`](scene.md) instance that you access through the read-only [`scene`](arview/scene.md) property. To the view’s [`Scene`](scene.md) instance you add one or more [`AnchorEntity`](anchorentity.md) instances that tell the view’s AR [`session`](arview/session.md) how to tether content to something in the real world. To each anchor, you attach a hierarchy of other [`Entity`](entity.md) instances that make up the content of the scene.

![Block diagram highlighting the AR view as the root object that you](https://docs-assets.developer.apple.com/published/c54620eff873984d5217d35fecb71e70/ARView-1%402x.png)

Additionally, you can use the view to:

- Configure render options, environmental characteristics, and the camera mode.
- Handle platform-appropriate user interaction in the form of mouse, keyboard, or gesture input.
- Find entities at a given point in the view.
- Access statistics and visualizations that help you debug your app.

Note that with [`ARView`](arview.md), a [`ModelEntity`](modelentity.md) casts a grounding shadow on a physical surface by default.  [`RealityView`](realityview.md) does not have this default behavior.

## Topics

### Creating a view
- [init(frame: CGRect)](arview/init(frame:).md)
  Creates an AR view with the specified dimensions.
- [init(frame: CGRect, cameraMode: ARView.CameraMode, automaticallyConfigureSession: Bool)](arview/init(frame:cameramode:automaticallyconfiguresession:).md)
  Creates an AR view with the specified dimensions, camera mode, and session configuration state.
- [init?(coder: NSCoder)](arview/init(coder:).md)
  Creates an AR view initialized from data in a given decoder.
- [convenience init(frame: CGRect, cameraMode: ARView.CameraMode)](arview/init(frame:cameramode:).md)
  Creates an AR view with the specified dimensions and camera mode.
### Working with the scene
- [var scene: Scene](arview/scene.md)
  The scene that the view renders and simulates.
### Configuring the AR session
- [var session: ARSession](arview/session.md)
  The AR session that supports the view’s rendering.
- [var automaticallyConfigureSession: Bool](arview/automaticallyconfiguresession.md)
  An indication of whether to use an automatically configured AR session.
- [var renderOptions: ARView.RenderOptions](arview/renderoptions-swift.property.md)
  The render options that configure the view’s AR session.
- [var renderCallbacks: ARView.RenderCallbacks](arview/rendercallbacks-swift.property.md)
  A container that holds the view’s render callbacks.
### Providing environmental context
- [var environment: ARView.Environment](arview/environment-swift.property.md)
  The view’s background, lighting, and acoustic properties.
- [var physicsOrigin: Entity?](arview/physicsorigin.md)
  The entity that defines the origin of the scene’s physics simulation.
- [var audioListener: Entity?](arview/audiolistener.md)
  The entity that defines the listener position and orientation for spatial audio.
### Managing the camera
- [var cameraMode: ARView.CameraMode](arview/cameramode-swift.property.md)
  A setting that chooses between the AR session’s camera and a virtual one.
- [var cameraTransform: Transform](arview/cameratransform.md)
  The transform of the currently active camera.
### Finding entities at a point in the view
- [func entity(at: CGPoint) -> Entity?](arview/entity(at:).md)
  Finds the entity in the AR scene closest to the specified point.
- [func entities(at: CGPoint) -> [Entity]](arview/entities(at:).md)
  Finds the collection of entities at the specified point in the scene.
- [func hitTest(CGPoint, query: CollisionCastQueryType, mask: CollisionGroup) -> [CollisionCastHit]](arview/hittest(_:query:mask:).md)
  Searches for objects corresponding to a point in the view based on a query and a collision mask.
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arview/hittest(_:types:).md)
  Searches for objects corresponding to a point in the view based on a set of result types.
- [func makeRaycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?](arview/makeraycastquery(from:allowing:alignment:).md)
  Creates a ray-cast query originating from a point in the view, centered on the camera’s field of view.
- [func raycast(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> [ARRaycastResult]](arview/raycast(from:allowing:alignment:).md)
  Performs a ray cast, where a ray is cast into the scene from the center of the camera through a point in the view, and the results are immediately returned.
- [func trackedRaycast(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment, updateHandler: ([ARRaycastResult]) -> Void) -> ARTrackedRaycast?](arview/trackedraycast(from:allowing:alignment:updatehandler:).md)
  Performs a tracked ray cast, where a ray is cast into the scene from the center of the camera through a point in the view.
### Adding gesture recognizers to entities
- [func installGestures(ARView.EntityGestures, for: any HasCollision) -> [any EntityGestureRecognizer]](arview/installgestures(_:for:).md)
  Installs standard gestures onto the given entity, configured to be recognized simultaneously.
- [func gestureRecognizer(UIGestureRecognizer, shouldRecognizeSimultaneouslyWith: UIGestureRecognizer) -> Bool](arview/gesturerecognizer(_:shouldrecognizesimultaneouslywith:).md)
### Mapping between coordinate spaces
- [func project(SIMD3<Float>) -> CGPoint?](arview/project(_:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the view.
- [func unproject(CGPoint, ontoPlane: float4x4, relativeToCamera: Bool) -> SIMD3<Float>?](arview/unproject(_:ontoplane:relativetocamera:).md)
  Unproject a 2D point from the view onto a plane in 3D world coordinates.
- [func unproject(CGPoint, ontoPlane: float4x4) -> SIMD3<Float>?](arview/unproject(_:ontoplane:).md)
  Maps a 2D point from the view’s coordinate system onto the given plane in 3D space.
- [func unproject(CGPoint, viewport: CGRect) -> SIMD3<Float>?](arview/unproject(_:viewport:).md)
  Maps a 2D point from the pixel coordinate system of a viewport into a 3D coordinate space. The point lies on this view’s near clipping plane.
- [func ray(through: CGPoint) -> (origin: SIMD3<Float>, direction: SIMD3<Float>)?](arview/ray(through:).md)
  Determines the position and direction of a ray through the given point in the 2D space of the view.
### Handling touch input
- [func touchesBegan(Set<UITouch>, with: UIEvent?)](arview/touchesbegan(_:with:).md)
  Tells the view that one or more new touches occurred.
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](arview/touchesmoved(_:with:).md)
  Tells the view when one or more touches associated with an event changed.
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](arview/touchesended(_:with:).md)
  Tells the view when one or more fingers are raised from the view.
- [func touchesCancelled(Set<UITouch>, with: UIEvent?)](arview/touchescancelled(_:with:).md)
  Tells the view when a system event (such as a system alert) cancels a touch sequence.
### Handling keyboard input
- [var acceptsFirstResponder: Bool](arview/acceptsfirstresponder.md)
  A Boolean value that indicates whether the view accepts first responder status.
- [func keyDown(with: NSEvent)](arview/keydown(with:).md)
  Informs the view that the user has pressed a key.
- [func keyUp(with: NSEvent)](arview/keyup(with:).md)
  Informs the view that the user has released a key.
### Handling mouse input
- [func mouseDown(with: NSEvent)](arview/mousedown(with:).md)
  Informs the view that the user has pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](arview/mousedragged(with:).md)
  Informs the view that the user has moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](arview/mouseup(with:).md)
  Informs the view that the user has released the left mouse button.
- [func mouseMoved(with: NSEvent)](arview/mousemoved(with:).md)
  Informs the view that the mouse has moved.
- [func rightMouseDown(with: NSEvent)](arview/rightmousedown(with:).md)
  Informs the view that the user has pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](arview/rightmousedragged(with:).md)
  Informs the view that the user has moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](arview/rightmouseup(with:).md)
  Informs the view that the user has released the right mouse button.
- [func otherMouseDown(with: NSEvent)](arview/othermousedown(with:).md)
  Informs the view that the user has pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](arview/othermousedragged(with:).md)
  Informs the view that the user has moved the mouse with a button other than the left or right button pressed.
- [func otherMouseUp(with: NSEvent)](arview/othermouseup(with:).md)
  Informs the view that the user has released a mouse button other than the left or right button.
- [func scrollWheel(with: NSEvent)](arview/scrollwheel(with:).md)
  Informs the view that the mouse’s scroll wheel has moved.
### Managing the view
- [var frame: NSRect](arview/frame.md)
  The frame rectangle, which describes the view’s location and size in the coordinate system of the view’s superview.
- [var contentScaleFactor: CGFloat](arview/contentscalefactor.md)
  The scale factor of the content in the view.
- [func didMoveToSuperview()](arview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func didMoveToWindow()](arview/didmovetowindow.md)
  Tells the view that its window property is set to a new value.
- [func layoutSubviews()](arview/layoutsubviews.md)
  Lays out subviews.
- [func layout()](arview/layout.md)
- [class var layerClass: AnyClass](arview/layerclass.md)
  The class used to create the layer for view instances.
- [func makeBackingLayer() -> CALayer](arview/makebackinglayer.md)
  Creates the view’s backing layer.
- [func viewDidChangeBackingProperties()](arview/viewdidchangebackingproperties.md)
  Tells the view when its backing store properties change.
- [func viewDidMoveToSuperview()](arview/viewdidmovetosuperview.md)
  Tells the view that it has a new superview or that the view’s superview has been removed.
### Taking a snapshot
- [func snapshot(saveToHDR: Bool, completion: (ARView.Image?) -> Void)](arview/snapshot(savetohdr:completion:)-66jzu.md)
  Takes a screenshot.
- [func snapshot(saveToHDR: Bool, completion: (ARView.Image?) -> Void)](arview/snapshot(savetohdr:completion:)-91ifk.md)
  Takes a screenshot.
- [typealias Image](arview/image.md)
### Debugging the session
- [Improving the Performance of a RealityKit App](improving-the-performance-of-a-realitykit-app.md)
  Measure CPU and GPU utilization to find ways to improve your app’s performance.
- [var debugOptions: ARView.DebugOptions](arview/debugoptions-swift.property.md)
  The current debugging options.
### Structures
- [ARView.DebugOptions](arview/debugoptions-swift.struct.md)
  Options for drawing overlay content in a scene that can aid in debugging.
- [ARView.EntityGestures](arview/entitygestures.md)
  The set of possible entity gesture recognizers.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.
- [ARView.PostProcessContext](arview/postprocesscontext.md)
  An object the framework uses to pass data to a postprocess callback.
- [ARView.RenderCallbacks](arview/rendercallbacks-swift.struct.md)
  A container that holds the view’s render callbacks.
- [ARView.RenderOptions](arview/renderoptions-swift.struct.md)
  The available rendering options that you use to selectively disable certain rendering effects.
### Instance Methods
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](arview/gesturerecognizer(_:shouldreceive:).md)
### Enumerations
- [ARView.CameraMode](arview/cameramode-swift.enum.md)
  The available camera modes.
### Default Implementations
- [ARSessionProviding Implementations](arview/arsessionproviding-implementations.md)

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [ARSessionProviding](../ARKit/ARSessionProviding.md)
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIGestureRecognizerDelegate](../UIKit/UIGestureRecognizerDelegate.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [ARView.DebugOptions](arview/debugoptions-swift.struct.md)
  Options for drawing overlay content in a scene that can aid in debugging.
- [typealias ARViewBase](arviewbase.md)
  The platform-specific base class for the view into which RealityKit renders content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview)*