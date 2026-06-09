# output::setOutputPosition

**Framework**: ComputeGraph  
**Kind**: func

Sets the position of the rendered output.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void output::setOutputPosition(float3 position)
```

#### Discussion

This function customizes where the particle will be rendered in 3D space. This affects only the rendered appearance and does not modify the particle node’s actual position.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/8ab44a94271235e51ad048ea460d6d35/output__setOutputPosition.svg)

## Parameters

- `position`: The 3D position where the output should be rendered, in the graph’s local coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setoutputposition)*