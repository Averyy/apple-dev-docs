# Drawing SpriteKit Content in a View

**Framework**: SpriteKit

Display visual content using SpriteKit.

#### Overview

Display SpriteKit content on the screen by configuring a SpriteKit renderer, its scene, and the visual objects you lay out on top of the scene. SpriteKit provides objects that are designed specifically for various types of content (see [`Nodes for Scene Building`](nodes-for-scene-building.md)), but for simplicity, this article displays an image in a view.

> **Note**:  There are other ways to draw SpriteKit content besides using a view. See [`Choosing a SpriteKit Scene Renderer`](choosing-a-spritekit-scene-renderer.md) for options.

![Screenshot of on the app window displaying an image (a sprite) using SpriteKit.](https://docs-assets.developer.apple.com/published/ced8e73de0c8478570ea46f6b7090c2e/media-3016873%402x.png)

Because the code in this article sets up a view, you put the lines from each of the following code listings into a view controller’s [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) function.

##### Create the Scene

Everything displayed with SpriteKit is done through a scene object, which is an instance of [`SKScene`](skscene.md). Use the following code to set up a basic scene:

```swift
let scene = SKScene(size: skView.bounds.size)

// Set the scene coordinates (0, 0) to the center of the screen.
scene.anchorPoint = CGPoint(x: 0.5, y: 0.5)
```

When you pass the `size` of the view’s `bounds` to the scene initializer, you size the scene to the view’s size. When you set the scene’s [`anchorPoint`](skscene/anchorpoint.md) to `(0.5, 0.5)`, you determine that the coordinates (0, 0) map to the center of the view.

For further discussion about how setting the `anchorPoint` changes an object’s position in the view, see [`Using the Anchor Point to Move the Sprite’s Frame`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/Sprites/Sprites.html#//apple_ref/doc/uid/TP40013043-CH9-SW36).

##### Lay Out Visual Content on Top of the Scene

You use node objects to display graphics in a SpriteKit view. SpriteKit provides different nodes depending on the content (see Nodes that Draw in  [`Nodes for Scene Building`](nodes-for-scene-building.md)). In this case, use an [`SKSpriteNode`](skspritenode.md) to display an image in the view:

```swift
let image = SKSpriteNode(imageNamed: "myImage.png")

// Add the image to the scene.
scene.addChild(image)

```

The functions to lay out content in a scene are covered in more detail in [`Accessing and Modifying the Node Tree`](accessing-and-modifying-the-node-tree.md).

##### Present the Scene Inside a View

After you set up the scene, you display it in the view by calling [`presentScene(_:)`](skview/presentscene(_:).md):

```swift
if let skView = self.view as? SKView { 
    skView.presentScene(scene)
}

```

Because the code in this article sets up a view, you add it to your view controller’s [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) function.

## See Also

- [class SKScene](skscene.md)
  An object that organizes all of the active SpriteKit content.
- [Nodes for Scene Building](nodes-for-scene-building.md)
  Define the appearance or layout of scene content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/drawing-spritekit-content-in-a-view)*