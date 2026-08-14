# SKView

**Framework**: SpriteKit  
**Kind**: class

A view subclass that renders a SpriteKit scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class SKView
```

## Mentions

- [Choosing a SpriteKit Scene Renderer](choosing-a-spritekit-scene-renderer.md)
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)

#### Overview

You present a scene by calling the view’s [`presentScene(_:)`](skview/presentscene(_:).md) method. When a scene is presented by the view, it alternates between running its simulation (which animates the content) and rendering the content for display. You can pause the scene by setting the view’s [`isPaused`](skview/ispaused.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

## Topics

### Displaying a Scene
- [var scene: SKScene?](skview/scene.md)
  The scene currently presented by this view.
- [func presentScene(SKScene?)](skview/presentscene(_:).md)
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](skview/presentscene(_:transition:).md)
  Transitions from the current scene to a new scene.
- [class SKTransition](sktransition.md)
  An object used to perform an animated transition to a new scene.
### Controlling the Timing of a Scene’s Rendering
- [var isPaused: Bool](skview/ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var preferredFramesPerSecond: Int](skview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [protocol SKViewDelegate](skviewdelegate.md)
  Methods to take custom control over the view’s render rate.
- [var frameInterval: Int](skview/frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.
- [var preferredFrameRate: Float](skview/preferredframerate.md)
### Configuring Performance Related Toggles
- [var ignoresSiblingOrder: Bool](skview/ignoressiblingorder.md)
  A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.
- [var shouldCullNonVisibleNodes: Bool](skview/shouldcullnonvisiblenodes.md)
  A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.
- [var allowsTransparency: Bool](skview/allowstransparency.md)
  A Boolean property that indicates whether the view is rendered using transparency.
- [var isAsynchronous: Bool](skview/isasynchronous.md)
  A Boolean value that indicates whether the content is rendered asynchronously.
### Enabling Visual Statistics for Debugging
- [var showsFPS: Bool](skview/showsfps.md)
  A Boolean value that indicates whether the view displays a frame rate indicator.
- [var showsNodeCount: Bool](skview/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](skview/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](skview/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](skview/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](skview/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.
### Converting Between View and Scene Coordinates
- [func convert(CGPoint, from: SKScene) -> CGPoint](skview/convert(_:from:).md)
  Converts a point from scene coordinates to view coordinates.
- [func convert(CGPoint, to: SKScene) -> CGPoint](skview/convert(_:to:).md)
  Converts a point from view coordinates to scene coordinates.
### Snapshotting Nodes to a Texture
- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](skview/texture(from:crop:).md)
  Renders a portion of a node’s contents and returns the rendered image as a texture.
- [func texture(from: SKNode) -> SKTexture?](skview/texture(from:).md)
  Renders the contents of a node tree and returns the rendered image as a texture.
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)
  Render a portion of the node tree into a new texture.
### Switching Renderers
- [Requesting the OpenGL Renderer](requesting-the-opengl-renderer.md)
  Switch to the legacy renderer temporarily for debugging purposes.
### Instance Properties
- [var disableDepthStencilBuffer: Bool](skview/disabledepthstencilbuffer.md)

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Choosing a SpriteKit Scene Renderer](choosing-a-spritekit-scene-renderer.md)
  Compare the different ways to display a SpriteKit scene.
- [class SKRenderer](skrenderer.md)
  An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.
- [class WKInterfaceSKScene](../watchkit/wkinterfaceskscene.md)
  A visual WatchKit element that displays a SpriteKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview)*