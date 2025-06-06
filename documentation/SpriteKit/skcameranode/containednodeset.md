# containedNodeSet()

**Framework**: SpriteKit  
**Kind**: method

Finds nodes that are visible in the camera’s viewport.

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
func containedNodeSet() -> Set<SKNode>
```

#### Return Value

The set of nodes that are in the same scene as the camera and contained in the camera’s viewport.

#### Discussion

The camera must be part of a scene’s node hierarchy and the scene must be presented in an view.

## See Also

- [func contains(SKNode) -> Bool](skcameranode/contains(_:).md)
  Checks to see if a node is visible in the camera’s viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skcameranode/containednodeset())*