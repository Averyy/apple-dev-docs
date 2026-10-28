# intersects(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether this node intersects the specified node.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func intersects(_ node: SKNode) -> Bool
```

```objc
- (BOOL) intersectsNode:(SKNode *) node;
```

## Return Value

[`true`](../../Swift/true.md) if the two nodes intersect; otherwise [`false`](../../Swift/false.md).

## Discussion

The two nodes are considered to intersect if their frames intersect. The children of both nodes are ignored in this test.

## Parameters

- `node`: Another node in the same node tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/intersects(_:))*