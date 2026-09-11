# pipelines

**Framework**: RealityKit  
**Kind**: property

The compiled pipelines used to execute the simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var pipelines: ComputeNodeGraph.Pipelines? { get set }
```

#### Discussion

When `nil`, the pipelines from [`resource`](computegraphcomponent/resource.md) are used. Assigning a value overrides the resource’s pipelines without replacing the loaded assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/pipelines)*