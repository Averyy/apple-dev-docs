# output::setColor

**Framework**: Compute Graph  
**Kind**: func

Sets the color of the rendered output.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::setColor(half4 color)
```

#### Discussion

This function customizes the color applied to the rendered particle output, including the alpha channel. This affects only the rendered appearance and does not modify the particle itself.

> **Note**: ![Graph](/images/com.apple.computegraph/output__setColor.svg)

## Parameters

- `color`: The RGBA color value to apply, using half-precision components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setcolor)*