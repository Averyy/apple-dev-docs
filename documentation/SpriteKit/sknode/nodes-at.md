# nodes(at:)

**Framework**: SpriteKit  
**Kind**: method

Returns an array of all visible descendants that intersect a point.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func nodes(at p: CGPoint) -> [SKNode]
```

## Mentions

- [Understanding Hit-Testing](understanding-hit-testing.md)
- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)

#### Return Value

An array of all `SKNode` objects in the subtree that intersect the point. Only nodes that have an [`isHidden`](sknode/ishidden.md) of `false` and an [`alpha`](sknode/alpha.md) greater that zero are included in the returned array. If no nodes intersect the point, an empty array is returned.

#### Discussion

A point is considered to be in a node if it lies inside the rectangle returned by the [`calculateAccumulatedFrame()`](sknode/calculateaccumulatedframe().md) method.

## Parameters

- `p`: A point in the node’s coordinate system.

## See Also

- [Understanding Hit-Testing](understanding-hit-testing.md)
  Learn how find child nodes at a given point by using hit-testing.
- [func contains(CGPoint) -> Bool](sknode/contains(_:).md)
  Returns a Boolean value that indicates whether a point lies inside the parent’s coordinate system.
- [func atPoint(CGPoint) -> SKNode](sknode/atpoint(_:).md)
  Returns the deepest visible descendant that intersects a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/nodes(at:))*