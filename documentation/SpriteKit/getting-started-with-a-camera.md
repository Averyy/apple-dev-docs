# Getting Started with a Camera

**Framework**: Spritekit

Learn the semantics of using a camera in your scene.

#### Overview

`SKCameraNode` defines which portion of a scene is visible on the screen. You must do the following to use a camera:

1. Instantiate a new `SKCameraNode` and set it as the scene’s [`camera`](skscene/camera.md).
2. Add the camera node as a child to the scene.

> **Note**:  If you don’t use a camera in your scene, the scene’s [`anchorPoint`](skscene/anchorpoint.md) is used to position the scene within the view.

Because the camera is a node, you define its position within the scene just like any other node. Actions, physics, and GameplayKit behaviors can also be applied to the camera node. When a scene is rendered using a camera node, the following occur:

- The scene is rendered so that the camera node’s origin is placed in the middle of the scene.
- The inverse of the camera node’s [`xScale`](sknode/xscale.md), [`yScale`](sknode/yscale.md), and [`zRotation`](sknode/zrotation.md) properties are applied to all nodes in the scene.

In this way, a camera’s position, scale, and rotation always have the opposite effect on how the scene is rendered. For example, if the camera is moved 10 pixels to the right, the scene is rendered as if everything else moved 10 pixels to the left. And similarly, if a camera node has an [`xScale`](sknode/xscale.md) and [`yScale`](sknode/yscale.md) of `2.0`, the scene is rendered as if every distance was half its normal size, effectively  increasing the visible area of the camera’s viewport.

> ❗ **Important**:  A camera’s descendants are always rendered relative to the camera node’s origin and without applying the camera’s scaling or rotation to them. For example, if your app displays scores or other data floating above the gameplay, the nodes that render these elements should be added as child nodes to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SpriteKit/getting-started-with-a-camera)*