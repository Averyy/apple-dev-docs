# Displaying 3D Content in a SpriteKit Scene

**Framework**: SpriteKit

Draw SceneKit content in a SpriteKit scene by using a 3D node.

#### Overview

SceneKit content rendered in SpriteKit is automatically assigned a camera and, because [`autoenablesDefaultLighting`](sk3dnode/autoenablesdefaultlighting.md) defaults to [`true`](https://developer.apple.com/documentation/swift/true), lights. That means you require very little code to add simple 3D primitives to your scene. The following code shows how to create a simple scene containing a torus and display it in a SpriteKit scene.

```swift
let scnScene: SCNScene = {
    let scnScene = SCNScene()
    
    let torusGeometry = SCNTorus(ringRadius: 10, pipeRadius: 3)
    let torusNode = SCNNode(geometry: torusGeometry)
    torusNode.eulerAngles = SCNVector3(x: CGFloat.pi / 2, y: 0, z: 0)
    scnScene.rootNode.addChildNode(torusNode)
    return scnScene
}()
     
let node = SK3DNode(viewportSize: CGSize(width: 200, height: 200))
node.scnScene = scnScene
```

After node is added to a [`SKScene`](skscene.md), the 3D torus is visible:

![SceneKit torus rendered in SpriteKit](https://docs-assets.developer.apple.com/published/317f4df1aa400a790e6776d1d28e9c09/media-2975459%402x.png)

##### Control How Your Content Is Rendered

Although [`SK3DNode`](sk3dnode.md) creates a default camera automatically, you can create your own camera for precise control over how the 3D content is rendered. The following code shows how you can create a 3D node with an explicitly created camera that looks at the first object in the SceneKit scene’s node tree.

```swift
let node = SK3DNode(viewportSize: CGSize(width: 200, height: 200))
node.position = position
node.scnScene = scnScene
node.name = "3dnode"
let camera = SCNCamera()
let cameraNode = SCNNode()
cameraNode.camera = camera
if let lookAtTarget = scnScene.rootNode.childNodes.first {
    
    let constraint = SCNLookAtConstraint(target: lookAtTarget)
    cameraNode.constraints = [ constraint ]
}
node.pointOfView = cameraNode
node.pointOfView?.position = SCNVector3(x: 0, y: 0, z: 20)
```

##### Set the Position and Orientation of Your 3d Content

You can create many instances of [`SK3DNode`](sk3dnode.md), each sharing the same SceneKit scene but each with an independent point of view. By updating the position of each 3D node’s point of view, you can create code that simulates a top-down, one-point perspective view. The following example shows how to do this by enumerating over all the nodes named `3dnode` in the `update` method of a [`SKSceneDelegate`](skscenedelegate.md).

```swift
scene.enumerateChildNodes(withName: "3dnode") {
    node, _ in
    if let node = node as? SK3DNode {
        let positionX = (width * 0.5 - node.position.x) / 10
        let positionY = (height * 0.5 - node.position.y) / 10
        node.pointOfView?.position = SCNVector3(x: positionX, y: positionY, z: 20)
    }
}
```

The following image shows how this code gives the impression of perspective inside SpriteKit:

![Top down perspective using SK3DNode](https://docs-assets.developer.apple.com/published/b9fb40b0a88164563095d4445fe3e8b9/media-3111362%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/displaying-3d-content-in-a-spritekit-scene)*