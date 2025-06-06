# referenceNode

**Framework**: SpriteKit  
**Kind**: property

The node whose coordinate system should be used to apply the constraint.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var referenceNode: SKNode? { get set }
```

#### Discussion

The default value is `nil`, meaning that the coordinate system of the node’s parent is used to apply the constraint. If another node is specified, all positions are converted into this node’s coordinate system before the constraint is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skconstraint/referencenode)*