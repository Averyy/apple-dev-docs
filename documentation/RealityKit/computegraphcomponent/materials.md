# materials

**Framework**: RealityKit  
**Kind**: property

The material used to render each graph output, keyed by output node identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var materials: [ComputeNodeGraph.NodeID : any Material] { get set }
```

#### Discussion

Assigning a [`resource`](computegraphcomponent/resource.md) initializes this dictionary from the materials the resource defines for its outputs. Assign a new value to replace them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/materials)*