# Positioning a Scene’s Origin Within its View

**Framework**: SpriteKit

Try the different ways to configure the scene’s origin inside its view.

#### Overview

You use the scene’s [`anchorPoint`](skscene/anchorpoint.md) to orient the default screen position of its nodes. For example, setting the scene’s `anchorPoint` to `(0,0)` makes child nodes with a position of `(0,0)` display at the bottom-left corner of the scene. However, setting the scene’s `anchorPoint` to `(0.5,0.5)` makes child nodes with a position of `(0,0)` display in the center of the scene.

You only use the scene’s `anchorPoint` for scene’s that don’t have a [`camera`](skscene/camera.md). If, however, you set a scene’s `camera`, then the camera drives which portion of the scene is visible at any given time, and the `anchorPoint` is ignored.

##### Set the Scenes Origin to the Bottom Left of Its View

By default, a scene’s origin is placed in the lower-left corner of the view, as shown in the figure below. A scene initialized with a height of `1024` and a width of `768` has the origin `(0,0)` in the lower-left corner, and the `(1024,768)` coordinate in the upper-right corner. The [`frame`](sknode/frame.md) property holds `(0,0)-(1024,768)`.

A scene’s [`position`](sknode/position.md) property is ignored by Scene Kit because the scene is always the root node for a node tree. Its default value is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGPoint/zero) and you can’t change it. However, you can move the scene’s origin by setting its [`anchorPoint`](skscene/anchorpoint.md) property. The anchor point is specified in the unit coordinate space and chooses a point in the enclosing view.

![Diagram showing that the default anchor for a scene is in the lower-left corner of the view](https://docs-assets.developer.apple.com/published/252784aad07f47ead2deaec28db29458/media-3020373%402x.png)

The default value for the anchor point is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGPoint/zero), which places it at the lower-left corner. The scene’s visible coordinate space is `(0,0)` to `(width,height)`. The default anchor point is most useful for games that do not scroll a scene’s content.

##### Center the Scenes Origin Within Its View

The second-most common anchor point value is `(0.5,0.5)`, which centers the scene’s origin in the middle of the view as shown in the figure below. The scene’s visible coordinate space is `(-width/2,-height/2)` to `(width/2,height/2)`. Centering the scene on its anchor point is most useful when you want to easily position nodes relative to the center of the screen, such as in a scrolling game. However, this effect is better achieved using a [`SKCameraNode`](skcameranode.md).

![Diagram showing that moving the anchor point to the center of the view is defined by the coordinates 0.5, 0.5.](https://docs-assets.developer.apple.com/published/082f7be89d0122e05eae1f4ab9afe87d/media-3020376%402x.png)

As a result of setting the `anchorPoint` and `size`, you indirectly set the scene’s frame, which determines the portion of the scene that’s visible to the user.

## See Also

- [var camera: SKCameraNode?](skscene/camera.md)
  The camera node in the scene that determines what part of the scene’s coordinate space is visible in the view.
- [var anchorPoint: CGPoint](skscene/anchorpoint.md)
  The point in the view’s frame that corresponds to the scene’s origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/positioning-a-scene-s-origin-within-its-view)*