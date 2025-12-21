# SKScene

**Framework**: SpriteKit  
**Kind**: class

An object that organizes all of the active SpriteKit content.

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
class SKScene
```

## Mentions

- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)
- [Customizing the Behavior of a Node](customizing-the-behavior-of-a-node.md)
- [Getting Started with Nodes](getting-started-with-nodes.md)
- [Subclassing Scenes Versus Assigning a Delegate](subclassing-scenes-versus-assigning-a-delegate.md)
- [Choosing a SpriteKit Scene Renderer](choosing-a-spritekit-scene-renderer.md)
- [Creating a Scene from a File](creating-a-scene-from-a-file.md)
- [Displaying 3D Content in a SpriteKit Scene](displaying-3d-content-in-a-spritekit-scene.md)
- [Drawing SpriteKit Content in a View](drawing-spritekit-content-in-a-view.md)
- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)

#### Overview

An [`SKScene`](skscene.md) object represents a scene of content in SpriteKit. A scene is the root node in a tree of SpriteKit nodes ([`SKNode`](sknode.md)). These nodes provide content that the scene animates and renders for display. To display a scene, you present it from an [`SKView`](skview.md), [`SKRenderer`](skrenderer.md), or [`WKInterfaceSKScene`](https://developer.apple.com/documentation/WatchKit/WKInterfaceSKScene).

`SKScene` is a subclass of [`SKEffectNode`](skeffectnode.md) and enables certain effects to apply to the entire scene. Though applying effects to an entire scene can be an expensive operation, creativity, and ingenuity may help you find some interesting ways to use effects.

## Topics

### Creating a Scene from a File
- [Creating a Scene from a File](creating-a-scene-from-a-file.md)
  Load a scene that you configure in Xcode’s scene editor.
### Creating a Scene Programmatically
- [init(size: CGSize)](skscene/init(size:).md)
  Initializes a new scene object.
- [var size: CGSize](skscene/size.md)
  The dimensions of the scene, in points.
### Stretching Content to Fit the View
- [Scaling a Scene’s Content to Fit the View](scaling-a-scene-s-content-to-fit-the-view.md)
  Configure the scale mode to determine how a scene is sized to fit its view.
- [var scaleMode: SKSceneScaleMode](skscene/scalemode.md)
  A setting that defines how the scene is mapped to the view that presents it.
- [enum SKSceneScaleMode](skscenescalemode.md)
  The modes that determine how the scene’s area is mapped to the view that presents it.
### Configuring the Viewport
- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
  Try the different ways to configure the scene’s origin inside its view.
- [var camera: SKCameraNode?](skscene/camera.md)
  The camera node in the scene that determines what part of the scene’s coordinate space is visible in the view.
- [var anchorPoint: CGPoint](skscene/anchorpoint.md)
  The point in the view’s frame that corresponds to the scene’s origin.
### Responding to Loading and Resizing Events
- [func sceneDidLoad()](skscene/scenedidload.md)
  Tells you when the scene is presented.
- [func didChangeSize(CGSize)](skscene/didchangesize(_:).md)
  Tells you when the scene’s size has changed.
- [func willMove(from: SKView)](skscene/willmove(from:).md)
  Tells you when the scene is about to be removed from a view.
- [func didMove(to: SKView)](skscene/didmove(to:).md)
  Tells you when the scene is presented by a view.
### Responding to Frame-Cycle Events
- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)
  Implement per-frame app logic, such as the scene’s update function that’s called every frame.
- [func update(TimeInterval)](skscene/update(_:).md)
  Tells your app to perform any app-specific logic to update your scene.
- [func didEvaluateActions()](skscene/didevaluateactions.md)
  Tells your app to peform any necessary logic after scene actions are evaluated.
- [func didSimulatePhysics()](skscene/didsimulatephysics.md)
  Tells your app to peform any necessary logic after physics simulations are performed.
- [func didApplyConstraints()](skscene/didapplyconstraints.md)
  Tells your app to peform any necessary logic after constraints are applied.
- [func didFinishUpdate()](skscene/didfinishupdate.md)
  Tells your app to peform any necessary logic after the scene has finished all of the steps required to process animations.
### Configuring a Delegate
- [Subclassing Scenes Versus Assigning a Delegate](subclassing-scenes-versus-assigning-a-delegate.md)
  Use a scene delegate to share app logic across various scenes.
- [var delegate: (any SKSceneDelegate)?](skscene/delegate.md)
  A delegate to be called during the animation loop.
- [protocol SKSceneDelegate](skscenedelegate.md)
  Methods that, when implemented, allow any class to participate in the SpriteKit render loop callbacks.
### Setting the Background Appearance
- [Creating a Scene with a Transparent Background](creating-a-scene-with-a-transparent-background.md)
  Set a transparent background color to show the content of the views below.
- [var view: SKView?](skscene/view.md)
  The view that is currently presenting the scene.
- [var backgroundColor: UIColor](skscene/backgroundcolor.md)
  The background color of the scene.
### Configuring Physics Properties
- [var physicsWorld: SKPhysicsWorld](skscene/physicsworld.md)
  The physics simulation associated with the scene.
### Adding Positional Audio
- [Using Audio Nodes with the Scene’s Listener](using-audio-nodes-with-the-scene-s-listener.md)
  Add audio to your scene, and optionally give it 2D-positional mixing characteristics.
- [var listener: SKNode?](skscene/listener.md)
  A node used to determine the position of the listener for positional audio in the scene.
- [var audioEngine: AVAudioEngine](skscene/audioengine.md)
  The AVFoundation audio engine used to play audio from audio nodes contained in the scene.
### Converting Between Coordinate Systems
- [func convertPoint(fromView: CGPoint) -> CGPoint](skscene/convertpoint(fromview:).md)
  Converts a point from view coordinates to scene coordinates.
- [func convertPoint(toView: CGPoint) -> CGPoint](skscene/convertpoint(toview:).md)
  Converts a point from scene coordinates to view coordinates.

## Relationships

### Inherits From
- [SKEffectNode](skeffectnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GKSceneRootNodeType](../GameplayKit/GKSceneRootNodeType.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [SKWarpable](skwarpable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Drawing SpriteKit Content in a View](drawing-spritekit-content-in-a-view.md)
  Display visual content using SpriteKit.
- [Nodes for Scene Building](nodes-for-scene-building.md)
  Define the appearance or layout of scene content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene)*