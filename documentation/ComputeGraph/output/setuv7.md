# output::setUV7

**Framework**: ComputeGraph  
**Kind**: func

Sets the seventh UV coordinate set for the rendered output mesh.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void output::setUV7(float4 value)
```

#### Discussion

This function assigns a custom UV coordinate to the seventh texture coordinate channel of the output mesh. If the mesh doesn’t already have a UV7 channel, it will be created. This enables multi-texturing and advanced shader effects.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/f60dc7f6eb244d129b8997ef2d015afe/output__setUV7.svg)

> **Note**: Reads and writes to output attribute `float4 uv7`

## Parameters

- `value`: The UV coordinate value to assign to all vertices in the output range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setuv7)*