# Getting Started with Spring Joints

**Framework**: SpriteKit

Connect two physics bodies with a spring joint.

#### Overview

The following Swift code shows how you can create a spring joint between sprite nodes. The physics body of `staticNode` has its [`isDynamic`](skphysicsbody/isdynamic.md) property set to [`false`](https://developer.apple.com/documentation/swift/false), preventing it from being affected by gravity. It is animated with an [`SKAction`](skaction.md) to move it upward.

`dynamicNode` is joined to `staticNode` with an [`SKPhysicsJointSpring`](skphysicsjointspring.md) named `spring`, with a frequency of 0.5 and a damping of 0.2.

The result is that as `staticNode` moves vertically, `dynamicNode` follows the upward path with a slight delay and bounce.

```swift
let scene = SKScene()
 
let size = CGSize(width: 50, height: 50)
 
let staticNode = SKSpriteNode(color: .red,
                              size: size)
let dynamicNode = SKSpriteNode(color: .blue,
                               size: size)
 
staticNode.physicsBody = SKPhysicsBody(rectangleOf: size)
staticNode.physicsBody?.isDynamic = false
staticNode.position = CGPoint(x: 250, y: 300)
 
dynamicNode.physicsBody = SKPhysicsBody(rectangleOf: size)
dynamicNode.position = CGPoint(x: 250, y: 200)
 
scene.addChild(staticNode)
scene.addChild(dynamicNode)
 
let spring = SKPhysicsJointSpring.joint(withBodyA: staticNode.physicsBody!,
                                        bodyB: dynamicNode.physicsBody!,
                                        anchorA: staticNode.position,
                                        anchorB: dynamicNode.position)
 
spring.frequency = 0.5
spring.damping = 0.2
 
scene.physicsWorld.add(spring)
 
let move = SKAction.moveBy(x:0, y: 200,
                           duration: 1)
staticNode.run(move)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/getting-started-with-spring-joints)*