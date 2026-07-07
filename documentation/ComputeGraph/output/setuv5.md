# output::setUV5

**Framework**: Compute Graph  
**Kind**: func

Sets the fifth UV coordinate set for the rendered output mesh.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::setUV5(float4 value)
```

#### Discussion

This function assigns a custom UV coordinate to the fifth texture coordinate channel of the output mesh. If the mesh doesn’t already have a UV5 channel, it will be created. This enables multi-texturing and advanced shader effects.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/3a0669cc958806322ce938b28511fc11/output__setUV5.svg)

> **Note**: Reads and writes to output attribute `float4 uv5`

## Parameters

- `value`: The UV coordinate value to assign to all vertices in the output range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setuv5)*