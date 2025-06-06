# Creating Position Constraints

**Framework**: SpriteKit

Create a position constraint and add it to a node.

#### Overview

You lock a node at a specific coordinate with [`positionX(_:y:)`](skconstraint/positionx(_:y:).md). Constrain a node’s horizontal position with [`positionX(_:)`](skconstraint/positionx(_:).md), or constrain its vertical position with [`positionY(_:)`](skconstraint/positiony(_:).md).

The following code shows how you can create a node with an attached physics body that’s affected by a noise field. The node moves with the noise but the constraints keep it within a rectangular region between 300 and 340 points on both the horizontal and vertical axes.

```swift
scene.physicsWorld.gravity = CGVector(dx: 0, dy: 0)
   
let noiseField = SKFieldNode.noiseField(withSmoothness: 1, animationSpeed: 0.1)
scene.addChild(noiseField)
     
let node = SKShapeNode(circleOfRadius: 10)
node.physicsBody = SKPhysicsBody(circleOfRadius: 10)
scene.addChild(node)
     
let range = SKRange(lowerLimit: 300, upperLimit: 340)

let lockToCenter = SKConstraint.positionX(range, y: range)

node.constraints = [ lockToCenter ]
```

## See Also

- [class func positionX(SKRange, y: SKRange) -> Self](skconstraint/positionx(_:y:).md)
  Creates a constraint that restricts both coordinates of a node’s position.
- [class func positionX(SKRange) -> Self](skconstraint/positionx(_:).md)
  Creates a constraint that restricts the x-coordinate of a node’s position.
- [class func positionY(SKRange) -> Self](skconstraint/positiony(_:).md)
  Creates a constraint that restricts the y-coordinate of a node’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-position-constraints)*