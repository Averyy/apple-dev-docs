# pointOfView

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The node from which the scene’s contents are viewed for rendering.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var pointOfView: SCNNode? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNNode * pointOfView;
```

## Discussion

Use a node with an [`SCNCamera`](../scncamera.md) instance assigned to its [`camera`](../scnnode/camera.md) property to view a scene. The node provides the position and direction of a virtual camera, and the camera object provides rendering parameters such as field of view and focus.

For debugging lights and shadows, you can also designate a spotlight (an [`SCNLight`](../scnlight.md) object whose [`type`](../scnlight/type.md) property is [`spot`](../scnlight/lighttype/spot.md)) as a point of view. In this case, the light’s [`spotInnerAngle`](../scnlight/spotinnerangle.md) property determines the field of view, and its [`zNear`](../scnlight/znear.md) and [`zFar`](../scnlight/zfar.md) properties determine the near and far extents of the region that is visible onscreen (also known as the *viewing frustum*).

In either case, the direction of view is along the negative z-axis of the node’s local coordinate space.

## See Also

### Managing Scene Display
- [var autoenablesDefaultLighting: Bool](./autoenablesdefaultlighting.md)
  A Boolean value that determines whether SceneKit automatically adds lights to a scene.
- [var isJitteringEnabled: Bool](./isjitteringenabled.md)
  A Boolean value that determines whether SceneKit applies jittering to reduce aliasing artifacts.
- [var showsStatistics: Bool](./showsstatistics.md)
  A Boolean value that determines whether SceneKit displays rendering performance statistics in an accessory view.
- [var debugOptions: SCNDebugOptions](./debugoptions.md)
  Options for drawing overlay content in a scene that can aid debugging.
- [var renderingAPI: SCNRenderingAPI](./renderingapi.md)
  The graphics technology SceneKit uses to render the scene.
- [struct SCNDebugOptions](../scndebugoptions.md)
  Options for drawing overlays with SceneKit content that can aid in debugging, used with the [`debugOptions`](./debugoptions.md) property.
- [enum SCNRenderingAPI](../scnrenderingapi.md)
  Options for choosing the graphics technology for an [`SCNView`](../scnview.md) object (or other SceneKit renderer) to use for drawing its contents. Used by the [`renderingAPI`](./renderingapi.md) property and the [`preferredRenderingAPI`](../scnview/option/preferredrenderingapi.md) option when initializing an [`SCNView`](../scnview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/pointofview)*