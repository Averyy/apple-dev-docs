# output::setUVTransform

**Framework**: ComputeGraph  
**Kind**: func

Sets the UV0 coordinate transformation for the rendered output.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void output::setUVTransform(float2 uvOffset, float2 uvScale)
```

#### Discussion

This function customizes how texture coordinates are applied to the rendered output by specifying an offset and scale. The UV transform affects texture mapping without modifying the underlying particle data.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/dc1c869d31a094ecd8e0a903c4885bb4/output__setUVTransform.svg)

## Parameters

- `uvOffset`: The offset to apply to UV0 coordinates.
- `uvScale`: The scale factor to apply to UV0 coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setuvtransform)*