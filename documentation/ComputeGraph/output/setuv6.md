# output::setUV6

**Framework**: ComputeGraph  
**Kind**: func

Sets the sixth UV coordinate set for the rendered output mesh.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void output::setUV6(float4 value)
```

#### Discussion

This function assigns a custom UV coordinate to the sixth texture coordinate channel of the output mesh. If the mesh doesn’t already have a UV6 channel, it will be created. This enables multi-texturing and advanced shader effects.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/2830f04298ff6ac83662ece24b59e16b/output__setUV6.svg)

> **Note**: Reads and writes to output attribute `float4 uv6`

## Parameters

- `value`: The UV coordinate value to assign to all vertices in the output range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setuv6)*