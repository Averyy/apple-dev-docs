# ARSKView

**Framework**: ARKit  
**Kind**: class

A view that blends virtual 2D content from SpriteKit into the 3D space of an augmented reality experience.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class ARSKView
```

## Mentions

- [Providing 2D Virtual Content with SpriteKit](providing-2d-virtual-content-with-spritekit.md)

#### Overview

Use the [`ARSKView`](arskview.md) class to create augmented reality experiences that position 2D elements in 3D space within a device camera view of the real world. When you run the view’s provided [`ARSession`](arsession.md) object:

- The view automatically renders the live video feed from the device camera as the scene background.
- When you implement [`ARSKViewDelegate`](arskviewdelegate.md) methods to associate SpriteKit content with real-world positions, the view automatically scales and rotates those SpriteKit nodes so that they appear to track the real world seen by the camera.

## Topics

### First Steps
- [Providing 2D Virtual Content with SpriteKit](providing-2d-virtual-content-with-spritekit.md)
  Use SpriteKit to place two-dimensional images in 3D space in your AR experience.
- [var session: ARSession](arskview/session.md)
  The AR session that manages motion tracking and camera image processing for the view’s contents.
### Responding to AR Updates
- [var delegate: (any ARSKViewDelegate)?](arskview/delegate.md)
  An object you provide to mediate synchronization of the view’s AR scene information with SpriteKit content.
- [protocol ARSKViewDelegate](arskviewdelegate.md)
  Methods you can implement to mediate the automatic synchronization of SpriteKit content with an AR session.
### Finding Real-World Surfaces
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arskview/hittest(_:types:).md)
  Searches for real-world objects or AR anchors in the captured camera image corresponding to a point in the SpriteKit view.
### Mapping Content to Real-World Positions
- [func anchor(for: SKNode) -> ARAnchor?](arskview/anchor(for:).md)
  Returns the AR anchor associated with the specified SpriteKit node, if any.
- [func node(for: ARAnchor) -> SKNode?](arskview/node(for:).md)
  Returns the SpriteKit node associated with the specified AR anchor, if any.

## Relationships

### Inherits From
- [SKView](../SpriteKit/SKView.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [@MainActor @preconcurrency struct RealityView<Content> where Content : View](../RealityKit/RealityView.md)
  A view that contains RealityKit content.
- [@MainActor @objc @preconcurrency class ARView](../RealityKit/ARView.md)
  A view that enables you to display an AR experience with RealityKit.
- [class ARSCNView](arscnview.md)
  A view that blends virtual 3D content from SceneKit into your augmented reality experience.
- [class ARCoachingOverlayView](arcoachingoverlayview.md)
  A view that displays standardized onboarding instructions to direct users toward a specific goal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview)*