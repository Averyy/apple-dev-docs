# validateAddingNode(_:)

**Framework**: RealityKit  
**Kind**: method

Validates that a node can be added to the graph without adding it, throwing a descriptive error if not.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func validateAddingNode(_ node: ShaderGraph.Node) throws
```

#### Discussion

Use [`canAddNode(_:)`](shadergraph/canaddnode(_:).md) instead when only a yes/no answer is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/validateaddingnode(_:))*