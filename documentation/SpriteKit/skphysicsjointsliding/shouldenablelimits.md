# shouldEnableLimits

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the sliding joint is restricted so that the objects may only slide a finite distance from the initial anchor point.

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
var shouldEnableLimits: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). If [`true`](https://developer.apple.com/documentation/Swift/true), then the [`lowerDistanceLimit`](skphysicsjointsliding/lowerdistancelimit.md) and [`upperDistanceLimit`](skphysicsjointsliding/upperdistancelimit.md) properties are used to limit the distance of the sliding joint.

## See Also

- [var lowerDistanceLimit: CGFloat](skphysicsjointsliding/lowerdistancelimit.md)
  The smallest distance allowed for the sliding joint.
- [var upperDistanceLimit: CGFloat](skphysicsjointsliding/upperdistancelimit.md)
  The largest distance allowed for the sliding joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/shouldenablelimits)*