# rayTestWithSegment(from:to:options:)

**Framework**: SceneKit  
**Kind**: method

Searches for physics bodies along a line segment between two points in the physics world.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func rayTestWithSegment(from origin: SCNVector3, to dest: SCNVector3, options: [SCNPhysicsWorld.TestOption : Any]? = nil) -> [SCNHitTestResult]
```

#### Return Value

An array of [`SCNHitTestResult`](scnhittestresult.md) objects describing search results.

#### Discussion

Use this method to implement concepts such as line of sight in your app. For example, in a game you might implement behavior for an enemy character by searching for physics bodies along a line between the enemy character’s position and the player character’s position, as illustrated below:

```objc
// Options: Look only for the closest object along line of sight,
// and use the collision bitmask to avoid finding the enemy itself.
NSDictionary *options = @{ SCNPhysicsTestSearchModeKey : SCNPhysicsTestSearchModeClosest,
                     SCNPhysicsTestCollisionBitMaskKey : @(kMyCategoryPlayer) };
 
NSArray *results = [physicsWorld rayTestWithSegmentFromPoint:enemy.position
                                                     toPoint:player.position
                                                     options:options];
if (results.firstObject.node == player) {
    // Enemy can see player: begin pursuit.
} else {
    // Enemy cannot see player: remain idle.
}
```

## Parameters

- `origin`: An endpoint of the line segment to search, specified in the scene’s world coordinate system.
- `dest`: The other endpoint of the line segment to search, specified in the scene’s world coordinate system.
- `options`: A dictionary of options affecting the test, or   to use default options. For applicable keys and the possible values, see  .

## See Also

- [func convexSweepTest(with: SCNPhysicsShape, from: SCNMatrix4, to: SCNMatrix4, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/convexsweeptest(with:from:to:options:).md)
  Searches for physics bodies in the space formed by moving a convex shape through the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/raytestwithsegment(from:to:options:))*