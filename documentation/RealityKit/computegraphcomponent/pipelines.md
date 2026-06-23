# pipelines

**Framework**: RealityKit  
**Kind**: property

The compiled pipelines used to execute the simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var pipelines: ComputeNodeGraph.Pipelines? { get set }
```

#### Discussion

When `nil`, the pipelines from [`resource`](computegraphcomponent/resource.md) are used. Assigning a value overrides the resource’s pipelines without replacing the loaded assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/pipelines)*