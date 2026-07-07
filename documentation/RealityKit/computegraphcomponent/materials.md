# materials

**Framework**: RealityKit  
**Kind**: property

Per-output material overrides, keyed by output node identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var materials: [ComputeNodeGraph.NodeID : any Material] { get set }
```

#### Discussion

When non-`nil`, these materials replace the corresponding materials defined in [`resource`](computegraphcomponent/resource.md). Set to `[:]` to restore resource-defined materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/materials)*