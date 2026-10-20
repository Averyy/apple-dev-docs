# contains(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a point lies inside the parent’s coordinate system.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
@MainActor
func contains(_ p: CGPoint) -> Bool
```

*macOS, watchOS*

```swift
func contains(_ p: CGPoint) -> Bool
```

```objc
- (BOOL) containsPoint:(CGPoint) p;
```

#### Return Value

[`true`](../../Swift/true.md) if the point lies inside the parent’s coordinate system; otherwise [`false`](../../Swift/false.md).

## Parameters

- `p`: A `CGPoint` to test against.

## See Also

### Hit Testing
- [Understanding Hit-Testing](../understanding-hit-testing.md)
  Learn how find child nodes at a given point by using hit-testing.
- [func atPoint(CGPoint) -> SKNode](./atpoint%28_%29.md)
  Returns the deepest visible descendant that intersects a point.
- [func nodes(at: CGPoint) -> [SKNode]](./nodes%28at%29.md)
  Returns an array of all visible descendants that intersect a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/contains(_:))*