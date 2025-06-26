# autoenablesDefaultLighting

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that determines whether Scene Kit automatically adds lights to a scene.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var autoenablesDefaultLighting: Bool { get set }
```

## Mentions

- [Displaying 3D Content in a SpriteKit Scene](displaying-3d-content-in-a-spritekit-scene.md)

#### Discussion

If this property’s value is [`true`](https://developer.apple.com/documentation/swift/true) (the default), SceneKit automatically adds and places an omnidirectional light source when rendering scenes that contain no lights or only contain ambient lights. If you change the value to false, the only light sources SceneKit uses for rendering a scene are those contained in the scene graph.

## See Also

- [var viewportSize: CGSize](sk3dnode/viewportsize.md)
  The size of the image rendered by the node.
- [var scnScene: SCNScene?](sk3dnode/scnscene.md)
  The SceneKit scene to render.
- [var pointOfView: SCNNode?](sk3dnode/pointofview.md)
  The Scene Kit node from which the scene’s contents are viewed when rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/autoenablesdefaultlighting)*