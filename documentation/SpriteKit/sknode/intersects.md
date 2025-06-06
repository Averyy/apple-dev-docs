# intersects(_:)

**Framework**: SpriteKit  
**Kind**: method

Returns a Boolean value that indicates whether this node intersects the specified node.

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
@MainActor
func intersects(_ node: SKNode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the two nodes intersect; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The two nodes are considered to intersect if their frames intersect. The children of both nodes are ignored in this test.

## Parameters

- `node`: Another node in the same node tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/intersects(_:))*