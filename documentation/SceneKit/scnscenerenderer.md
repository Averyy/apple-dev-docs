# SCNSceneRenderer

**Framework**: SceneKit  
**Kind**: protocol

Methods and properties common to the [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md), and [`SCNRenderer`](scnrenderer.md) classes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol SCNSceneRenderer : NSObjectProtocol
```

#### Overview

You use an instance of one of these classes to display a scene and manage SceneKit’s rendering and animation of the scene’s contents.

Typically, you use the [`SCNView`](scnview.md) class to display a scene in a window (or full screen). You can create and configure a SceneKit view programmatically or in Interface Builder. The other renderer classes render SceneKit content in more specialized situations. If your app has a user interface composed of Core Animation layers, you can use the [`SCNLayer`](scnlayer.md) class to render a scene into a layer. If your app uses Metal or OpenGL for other rendering, you can use the [`SCNRenderer`](scnrenderer.md) class to render SceneKit content with the same Metal device or OpenGL context.

Use the [`scene`](scnscenerenderer/scene.md) property of the view, layer, or renderer to specify the scene to display.

## Topics

### Presenting a Scene
- [var scene: SCNScene?](scnscenerenderer/scene.md)
  The scene to be displayed.
- [func present(SCNScene, with: SKTransition, incomingPointOfView: SCNNode?, completionHandler: (() -> Void)?)](scnscenerenderer/present(_:with:incomingpointofview:completionhandler:).md)
  Displays the specified scene with an animated transition.
### Managing Scene Display
- [var pointOfView: SCNNode?](scnscenerenderer/pointofview.md)
  The node from which the scene’s contents are viewed for rendering.
- [var autoenablesDefaultLighting: Bool](scnscenerenderer/autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var isJitteringEnabled: Bool](scnscenerenderer/isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var showsStatistics: Bool](scnscenerenderer/showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var debugOptions: SCNDebugOptions](scnscenerenderer/debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [var renderingAPI: SCNRenderingAPI](scnscenerenderer/renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [struct SCNDebugOptions](scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](scnscenerenderer/debugoptions.md) property.
- [enum SCNRenderingAPI](scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](scnscenerenderer/renderingapi.md) property and the [`preferredRenderingAPI`](scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](scnview.md) object.
### Managing Scene Animation Timing
- [var sceneTime: TimeInterval](scnscenerenderer/scenetime.md)
  The current scene time.
- [var isPlaying: Bool](scnscenerenderer/isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var loops: Bool](scnscenerenderer/loops.md)
  A Boolean value that determines whether SceneKit restarts the scene time after all animations in the scene have played.
### Preloading Renderer Resources
- [func prepare(Any, shouldAbortBlock: (() -> Bool)?) -> Bool](scnscenerenderer/prepare(_:shouldabortblock:).md)
  Prepares a SceneKit object for rendering.
- [func prepare([Any], completionHandler: ((Bool) -> Void)?)](scnscenerenderer/prepare(_:completionhandler:).md)
  Prepares the specified SceneKit objects for rendering, using a background thread.
### Working With Projected Scene Contents
- [func hitTest(CGPoint, options: [SCNHitTestOption : Any]?) -> [SCNHitTestResult]](scnscenerenderer/hittest(_:options:).md)
  Searches the renderer’s scene for objects corresponding to a point in the rendered image.
- [struct SCNHitTestOption](scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.
- [func isNode(SCNNode, insideFrustumOf: SCNNode) -> Bool](scnscenerenderer/isnode(_:insidefrustumof:).md)
  Returns a Boolean value indicating whether a node might be visible from a specified point of view.
- [func nodesInsideFrustum(of: SCNNode) -> [SCNNode]](scnscenerenderer/nodesinsidefrustum(of:).md)
  Returns all nodes that might be visible from a specified point of view.
- [func projectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/projectpoint(_:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the renderer.
- [func unprojectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/unprojectpoint(_:).md)
  Unprojects a point from the 2D pixel coordinate system of the renderer to the 3D world coordinate system of the scene.
### Participating in the Scene Rendering Process
- [var delegate: (any SCNSceneRendererDelegate)?](scnscenerenderer/delegate.md)
  A delegate object that receives messages about SceneKit’s rendering process.
### Customizing Scene Rendering with Metal
- [var currentRenderCommandEncoder: (any MTLRenderCommandEncoder)?](scnscenerenderer/currentrendercommandencoder.md)
  The Metal render command encoder in use for the current SceneKit rendering pass.
- [var device: (any MTLDevice)?](scnscenerenderer/device.md)
  The Metal device this renderer uses for rendering.
- [var commandQueue: (any MTLCommandQueue)?](scnscenerenderer/commandqueue.md)
  The Metal command queue this renderer uses for rendering.
- [var colorPixelFormat: MTLPixelFormat](scnscenerenderer/colorpixelformat.md)
  The Metal pixel format for the renderer’s color output.
- [var depthPixelFormat: MTLPixelFormat](scnscenerenderer/depthpixelformat.md)
  The Metal pixel format for the renderer’s depth buffer.
- [var stencilPixelFormat: MTLPixelFormat](scnscenerenderer/stencilpixelformat.md)
  The Metal pixel format for the renderer’s stencil buffer.
### Customizing Scene Rendering with OpenGL
- [var context: UnsafeMutableRawPointer?](scnscenerenderer/context.md)
  The OpenGL rendering context that SceneKit uses for rendering the scene.
### Rendering Sprite Kit Content over a Scene
- [var overlaySKScene: SKScene?](scnscenerenderer/overlayskscene.md)
  A Sprite Kit scene to be rendered on top of the SceneKit content.
### Working With Positional Audio
- [var audioListener: SCNNode?](scnscenerenderer/audiolistener.md)
  The node representing the listener’s position in the scene for use with positional audio effects.
- [var audioEnvironmentNode: AVAudioEnvironmentNode](scnscenerenderer/audioenvironmentnode.md)
  The 3D audio mixing node SceneKit uses for positional audio effects.
- [var audioEngine: AVAudioEngine](scnscenerenderer/audioengine.md)
  The audio engine SceneKit uses for playing scene sounds.
### Instance Properties
- [var currentRenderPassDescriptor: MTLRenderPassDescriptor](scnscenerenderer/currentrenderpassdescriptor.md)
- [var currentTime: TimeInterval](scnscenerenderer/currenttime.md)
- [var currentViewport: CGRect](scnscenerenderer/currentviewport.md)
- [var isTemporalAntialiasingEnabled: Bool](scnscenerenderer/istemporalantialiasingenabled.md)
- [var usesReverseZ: Bool](scnscenerenderer/usesreversez.md)
- [var workingColorSpace: CGColorSpace](scnscenerenderer/workingcolorspace.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SCNLayer](scnlayer.md)
- [SCNRenderer](scnrenderer.md)
- [SCNView](scnview.md)

## See Also

- [protocol SCNSceneRendererDelegate](scnscenerendererdelegate.md)
  Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.
- [class SCNLayer](scnlayer.md)
  A Core Animation layer that renders a SceneKit scene as its content.
- [class SCNRenderer](scnrenderer.md)
  A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.
- [class SCNHitTestResult](scnhittestresult.md)
  Information about the result of a scene-space or view-space search for scene elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer)*