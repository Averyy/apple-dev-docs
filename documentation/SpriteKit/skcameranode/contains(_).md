# contains(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Checks to see if a node is visible in the camera’s viewport.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contains(_ node: SKNode) -> Bool
```

```objc
- (BOOL) containsNode:(SKNode *) node;
```

#### Return Value

[`true`](../../Swift/true.md) if the node in the same scene and inside the camera’s viewport; otherwise [`false`](../../Swift/false.md).

#### Discussion

The camera must be part of a scene’s node hierarchy and the scene must be presented in an view.

## Parameters

- `node`: An [`SKNode`](../sknode.md) object.

## See Also

### Node Visibility
- [func containedNodeSet() -> Set<SKNode>](./containednodeset%28%29.md)
  Finds nodes that are visible in the camera’s viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skcameranode/contains(_:))*