# canAddNode(with:)

**Framework**: Compute Graph  
**Kind**: method

Whether a node with the given definition can be used in this stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
func canAddNode(with definition: ComputeNodeGraph.NodeDefinition) -> Bool
```

#### Discussion

Use as a preflight check — for example, to enable a “drop here” target in a node-graph editor, or to filter a library down to definitions valid for a particular stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/stage/canaddnode(with:))*