# SK3DNode

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

3D SceneKit content drawn as a flattened sprite.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SK3DNode
```

```objc
@interface SK3DNode : SKNode
```

## Mentions

- [Displaying 3D Content in a SpriteKit Scene](./displaying-3d-content-in-a-spritekit-scene.md)

#### Overview

Use [`SK3DNode`](./sk3dnode.md) objects to incorporate 3D SceneKit content into a SpriteKit-based game. When SpriteKit renders the node, the SceneKit scene is animated and rendered first. Then this rendered image is composited into the SpriteKit scene. Use the [`scnScene`](./sk3dnode/scnscene.md) property to specify the SceneKit scene to be rendered.

## Topics

### Getting Started with 3D Node
- [Displaying 3D Content in a SpriteKit Scene](./displaying-3d-content-in-a-spritekit-scene.md)
  Draw SceneKit content in a SpriteKit scene by using a 3D node.
### Creating 3D Nodes
- [init(viewportSize: CGSize)](./sk3dnode/init%28viewportsize%29.md)
  Initializes a new 3D node.
- [init?(coder: NSCoder)](./sk3dnode/init%28coder%29.md)
  Tells you when to initialize a 3D node that has been unarchived.
### Configuring a 3D Node
- [var viewportSize: CGSize](./sk3dnode/viewportsize.md)
  The size of the image rendered by the node.
- [var scnScene: SCNScene?](./sk3dnode/scnscene.md)
  The SceneKit scene to render.
- [var pointOfView: SCNNode?](./sk3dnode/pointofview.md)
  The Scene Kit node from which the scene’s contents are viewed when rendered.
- [var autoenablesDefaultLighting: Bool](./sk3dnode/autoenablesdefaultlighting.md)
  A Boolean value that determines whether Scene Kit automatically adds lights to a scene.
### Animating a 3D Node’s Content in Scene Kit
- [var isPlaying: Bool](./sk3dnode/isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var loops: Bool](./sk3dnode/loops.md)
  A Boolean value that determines whether Scene Kit restarts the scene time after all animations in the scene have played.
- [var sceneTime: TimeInterval](./sk3dnode/scenetime.md)
  The current scene time.
### Projecting Points and Performing Hit-Testing
- [func hitTest(CGPoint, options: [String : Any]?) -> [SCNHitTestResult]](./sk3dnode/hittest%28_,options%29.md)
  Searches the Scene Kit scene for objects corresponding to a point in the rendered image.
- [func projectPoint(vector_float3) -> vector_float3](./sk3dnode/projectpoint%28_%29.md)
  Projects a point from the 3D world coordinate system of the SceneKit scene to the 2D viewport coordinate system of the SpriteKit node.
- [func unprojectPoint(vector_float3) -> vector_float3](./sk3dnode/unprojectpoint%28_%29.md)
  Unprojects a point from the SpriteKit node’s 2D viewport coordinate system to the 3D world coordinate system of the SceneKit scene.

## Relationships

### Inherits From
- [SKNode](./sknode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Nodes that Draw
- [Maximizing Node Drawing Performance](./maximizing-node-drawing-performance.md)
  Structure your nodes for maximum performance.
- [class SKSpriteNode](./skspritenode.md)
  An image or solid color.
- [class SKShapeNode](./skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKEmitterNode](./skemitternode.md)
  A source of various particle effects.
- [class SKLabelNode](./sklabelnode.md)
  A graphical element that draws text.
- [class SKVideoNode](./skvideonode.md)
  A graphical element that plays video content.
- [class SKTileMapNode](./sktilemapnode.md)
  A two-dimensional array of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode)*