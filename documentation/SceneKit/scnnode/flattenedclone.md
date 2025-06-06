# flattenedClone()

**Framework**: SceneKit  
**Kind**: method

Creates an optimized copy of the node and its children.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func flattenedClone() -> Self
```

#### Return Value

A new single node containing the combined geometries and materials of the node and its child node subtree.

#### Discussion

Rendering complex node hierarchies can incur a performance cost. Each geometry and material requires a separate draw command to be sent to the GPU, and each draw command comes with a performance overhead. If you plan for a portion of your scene’s node hierarchy to remain static (with respect to itself, if not the rest of the scene), use this method to create a single node containing all elements of that node hierarchy that SceneKit can render using fewer draw commands.

## See Also

- [func clone() -> Self](scnnode/clone.md)
  Creates a copy of the node and its children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/flattenedclone())*