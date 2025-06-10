# contains(_:)

**Framework**: SpriteKit  
**Kind**: method

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
@MainActor
func contains(_ node: SKNode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the node in the same scene and inside the camera’s viewport; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The camera must be part of a scene’s node hierarchy and the scene must be presented in an view.

## Parameters

- `node`: An   object.

## See Also

- [func containedNodeSet() -> Set<SKNode>](skcameranode/containednodeset.md)
  Finds nodes that are visible in the camera’s viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skcameranode/contains(_:))*