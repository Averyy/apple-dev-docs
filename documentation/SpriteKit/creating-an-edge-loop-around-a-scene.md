# Creating an Edge Loop Around a Scene

**Framework**: SpriteKit

Border your scene with an obstacle that physics bodies cannot penetrate.

#### Overview

When you want to confine your in-app objects to a specific region, use an edge-based physics body to define the area. In an app that models a pool table, for example, the balls are the in-app objects, and the table edges collectively create an *edge loop*. The following code demonstrates creating an edge loop to implement an impenetrable boundary that extends from edge to edge in the scene.

**Swift**:

```swift
func createSceneContents() {
    self.backgroundColor = .black
    self.scaleMode = .aspectFit
    self.physicsBody = SKPhysicsBody(edgeLoopFrom: self.frame)
}
```

**Obj-C**:

```objc
- (void) createSceneContents
{
    self.backgroundColor = [SKColor blackColor];
    self.scaleMode = SKSceneScaleModeAspectFit;
    self.physicsBody = [SKPhysicsBody bodyWithEdgeLoopFromRect:self.frame];
}
```

## See Also

- [init(edgeLoopFrom: CGRect)](skphysicsbody/init(edgeloopfrom:)-8sqfy.md)
  Creates an edge loop from a rectangle.
- [init(edgeFrom: CGPoint, to: CGPoint)](skphysicsbody/init(edgefrom:to:).md)
  Creates an edge between two points.
- [init(edgeLoopFrom: CGPath)](skphysicsbody/init(edgeloopfrom:)-5grxu.md)
  Creates an edge loop from a path.
- [init(edgeChainFrom: CGPath)](skphysicsbody/init(edgechainfrom:).md)
  Creates an edge chain from a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-an-edge-loop-around-a-scene)*