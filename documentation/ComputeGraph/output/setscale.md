# output::setScale

**Framework**: Compute Graph  
**Kind**: func

Sets the scale factor of the rendered output.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::setScale(float2 scale)
```

#### Discussion

This function applies a scale transformation to the rendered particle output, allowing independent control of horizontal and vertical scaling. This affects only the rendered appearance and does not modify the particle itself.

> **Note**: ![Graph](/images/com.apple.computegraph/output__setScale.svg)

## Parameters

- `scale`: The scale factor to apply in X and Y dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setscale)*