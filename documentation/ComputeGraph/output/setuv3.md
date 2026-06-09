# output::setUV3

**Framework**: ComputeGraph  
**Kind**: func

Sets the third UV coordinate set for the rendered output mesh.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void output::setUV3(float4 value)
```

#### Discussion

This function assigns a custom UV coordinate to the third texture coordinate channel of the output mesh. If the mesh doesn’t already have a UV3 channel, it will be created. This enables multi-texturing and advanced shader effects.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/dc15f4ea8ed7dbebea493703d5a3c2fe/output__setUV3.svg)

> **Note**: Reads and writes to output attribute `float4 uv3`

## Parameters

- `value`: The UV coordinate value to assign to all vertices in the output range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setuv3)*