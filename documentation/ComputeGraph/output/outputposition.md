# output::outputPosition

**Framework**: ComputeGraph  
**Kind**: func

Returns the position of the rendered output.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
float3 output::outputPosition()
```

#### Return Value

The 3D position of the rendered output in the graph’s local coordinate system.

#### Discussion

This function retrieves the 3D position where the particle will be rendered, which may differ from the particle node’s actual position if output transformations have been applied.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/2f3c4e2a21d75a156cdd0a6e0d34587b/output__outputPosition.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/outputposition)*