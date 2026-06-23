# canAddNode(with:)

**Framework**: ComputeGraph  
**Kind**: method

Whether a node with the given definition can be used in this stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
func canAddNode(with definition: ComputeNodeGraph.NodeDefinition) -> Bool
```

#### Discussion

Use as a preflight check — for example, to enable a “drop here” target in a node-graph editor, or to filter a library down to definitions valid for a particular stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/stage/canaddnode(with:))*