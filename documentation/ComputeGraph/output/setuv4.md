# output::setUV4

**Framework**: Compute Graph  
**Kind**: func

Sets the fourth UV coordinate set for the rendered output mesh.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::setUV4(float4 value)
```

#### Discussion

This function assigns a custom UV coordinate to the fourth texture coordinate channel of the output mesh. If the mesh doesn’t already have a UV4 channel, it will be created. This enables multi-texturing and advanced shader effects.

> **Note**: ![Graph](/images/com.apple.computegraph/output__setUV4.svg)

> **Note**: Reads and writes to output attribute `float4 uv4`

## Parameters

- `value`: The UV coordinate value to assign to all vertices in the output range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setuv4)*