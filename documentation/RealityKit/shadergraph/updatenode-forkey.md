# updateNode(_:forKey:)

**Framework**: RealityKit  
**Kind**: method

Replaces the node stored under the given name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func updateNode(_ node: ShaderGraph.Node, forKey name: String) throws
```

#### Discussion

Any existing edges referencing `name` are preserved and will refer to the updated node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/updatenode(_:forkey:))*