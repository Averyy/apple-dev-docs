# contains(_:)

**Framework**: SpriteKit  
**Kind**: method

Returns a Boolean value that indicates whether a point lies inside the parent’s coordinate system.

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
func contains(_ p: CGPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the point lies inside the parent’s coordinate system; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `p`: A   to test against.

## See Also

- [Understanding Hit-Testing](understanding-hit-testing.md)
  Learn how find child nodes at a given point by using hit-testing.
- [func atPoint(CGPoint) -> SKNode](sknode/atpoint(_:).md)
  Returns the deepest visible descendant that intersects a point.
- [func nodes(at: CGPoint) -> [SKNode]](sknode/nodes(at:).md)
  Returns an array of all visible descendants that intersect a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/contains(_:))*