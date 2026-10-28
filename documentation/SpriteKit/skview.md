# SKView

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A view subclass that renders a SpriteKit scene.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class SKView
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface SKView : UIView
```

*macOS*

```objc
@interface SKView : NSView
```

## Mentions

- [Choosing a SpriteKit Scene Renderer](./choosing-a-spritekit-scene-renderer.md)
- [Creating a New Node By Rendering To a Texture](./creating-a-new-node-by-rendering-to-a-texture.md)

## Overview

You present a scene by calling the view’s [`presentScene(_:)`](./skview/presentscene%28_%29.md) method. When a scene is presented by the view, it alternates between running its simulation (which animates the content) and rendering the content for display. You can pause the scene by setting the view’s [`isPaused`](./skview/ispaused.md) property to [`true`](../Swift/true.md).

## Topics

### Displaying a Scene
- [var scene: SKScene?](./skview/scene.md)
  The scene currently presented by this view.
- [func presentScene(SKScene?)](./skview/presentscene%28_%29.md)
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](./skview/presentscene%28_,transition%29.md)
  Transitions from the current scene to a new scene.
- [class SKTransition](./sktransition.md)
  An object used to perform an animated transition to a new scene.
### Controlling the Timing of a Scene’s Rendering
- [var isPaused: Bool](./skview/ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var preferredFramesPerSecond: Int](./skview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](./skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](./skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var frameInterval: Int](./skview/frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.
- [var preferredFrameRate: Float](./skview/preferredframerate.md)
### Configuring Performance Related Toggles
- [var ignoresSiblingOrder: Bool](./skview/ignoressiblingorder.md)
  A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.
- [var shouldCullNonVisibleNodes: Bool](./skview/shouldcullnonvisiblenodes.md)
  A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.
- [var allowsTransparency: Bool](./skview/allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.
- [var isAsynchronous: Bool](./skview/isasynchronous.md)
  A Boolean value that indicates whether the content is rendered asynchronously.
### Enabling Visual Statistics for Debugging
- [var showsFPS: Bool](./skview/showsfps.md)
  A Boolean value that indicates whether the view displays a frame rate indicator.
- [var showsNodeCount: Bool](./skview/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](./skview/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](./skview/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](./skview/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](./skview/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.
### Converting Between View and Scene Coordinates
- [func convert(CGPoint, from: SKScene) -> CGPoint](./skview/convert%28_,from%29.md)
  Converts a point from scene coordinates to view coordinates.
- [func convert(CGPoint, to: SKScene) -> CGPoint](./skview/convert%28_,to%29.md)
  Converts a point from view coordinates to scene coordinates.
### Snapshotting Nodes to a Texture
- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](./skview/texture%28from,crop%29.md)
  Renders a portion of a node’s contents and returns the rendered image as a texture.
- [func texture(from: SKNode) -> SKTexture?](./skview/texture%28from%29.md)
  Renders the contents of a node tree and returns the rendered image as a texture.
- [Creating a New Node By Rendering To a Texture](./creating-a-new-node-by-rendering-to-a-texture.md)
  Render a portion of the node tree into a new texture.
### Switching Renderers
- [Requesting the OpenGL Renderer](./requesting-the-opengl-renderer.md)
  Switch to the legacy renderer temporarily for debugging purposes.
### Instance Properties
- [var disableDepthStencilBuffer: Bool](./skview/disabledepthstencilbuffer.md)

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
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

### Scene Renderers
- [Choosing a SpriteKit Scene Renderer](./choosing-a-spritekit-scene-renderer.md)
  Compare the different ways to display a SpriteKit scene.
- [class SKRenderer](./skrenderer.md)
  An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.
- [class WKInterfaceSKScene](../WatchKit/wkinterfaceskscene.md)
  A visual WatchKit element that displays a SpriteKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview)*