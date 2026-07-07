# models

**Framework**: RealityKit  
**Kind**: property

Per-output model component overrides, keyed by output node identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var models: [ComputeNodeGraph.NodeID : ModelComponent] { get set }
```

#### Discussion

When non-`nil`, these model components replace those defined in [`resource`](computegraphcomponent/resource.md). Set to `[:]` to restore resource-defined models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/models)*