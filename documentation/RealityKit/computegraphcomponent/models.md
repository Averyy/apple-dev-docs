# models

**Framework**: RealityKit  
**Kind**: property

The model component used to render each graph output, keyed by output node identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var models: [ComputeNodeGraph.NodeID : ModelComponent] { get set }
```

#### Discussion

Assigning a [`resource`](computegraphcomponent/resource.md) initializes this dictionary from the models the resource defines for its outputs. Assign a new value to replace them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/models)*