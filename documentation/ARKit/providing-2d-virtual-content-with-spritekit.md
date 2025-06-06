# Providing 2D Virtual Content with SpriteKit

**Framework**: ARKit

Use SpriteKit to place two-dimensional images in 3D space in your AR experience.

#### Overview

SpriteKit is inherently for 2D visual content, but augmented reality involves real-world 3D spaces. Use the [`ARSKView`](arskview.md) class to create AR experiences by providing 2D sprites ([`SKNode`](https://developer.apple.com/documentation/SpriteKit/SKNode) objects) that correspond to real-world 3D positions ([`ARAnchor`](aranchor.md) objects). When the user moves the device, the view automatically rotates and scales the SpriteKit nodes corresponding to anchors so that they appear to track the real world seen by the camera.

For example, you can place 2D images that appear to float in 3D space:

```swift
// Create a transform with a translation of 0.2 meters in front of the camera.
var translation = matrix_identity_float4x4
translation.columns.3.z = -0.2
let transform = simd_mul(view.session.currentFrame.camera.transform, translation)

// Add a new anchor to the session.
let anchor = ARAnchor(transform: transform)
view.session.add(anchor: anchor)

// (Elsewhere...) Provide a label node to represent the anchor.
func view(_ view: ARSKView, nodeFor anchor: ARAnchor) -> SKNode? {
    return SKLabelNode(text: "👾")
}
```

The [`view(_:nodeFor:)`](arskviewdelegate/view(_:nodefor:).md) method above returns an [`SKLabelNode`](https://developer.apple.com/documentation/SpriteKit/SKLabelNode) object, which displays a text label. Like most SpriteKit nodes, this class creates a 2D visual representation, so the [`ARSKView`](arskview.md) class presents the node in a billboard style: The sprite scales and rotates (around its z-axis) so that it appears to follow the 3D position of its anchor, but always faces toward the camera.

## See Also

- [var session: ARSession](arskview/session.md)
  The AR session that manages motion tracking and camera image processing for the view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/providing-2d-virtual-content-with-spritekit)*