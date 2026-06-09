# output::setColor

**Framework**: ComputeGraph  
**Kind**: func

Sets the color of the rendered output.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void output::setColor(half4 color)
```

#### Discussion

This function customizes the color applied to the rendered particle output, including the alpha channel. This affects only the rendered appearance and does not modify the particle itself.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/3ff0d83afa0e68eac4cf4da113c5e3ef/output__setColor.svg)

## Parameters

- `color`: The RGBA color value to apply, using half-precision components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setcolor)*