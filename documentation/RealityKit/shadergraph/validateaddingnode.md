# validateAddingNode(_:)

**Framework**: RealityKit  
**Kind**: method

Validates that a node can be added to the graph without adding it, throwing a descriptive error if not.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func validateAddingNode(_ node: ShaderGraph.Node) throws
```

#### Discussion

Use [`canAddNode(_:)`](shadergraph/canaddnode(_:).md) instead when only a yes/no answer is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/validateaddingnode(_:))*