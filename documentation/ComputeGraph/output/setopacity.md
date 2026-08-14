# output::setOpacity

**Framework**: Compute Graph  
**Kind**: func

Sets the opacity of the rendered output.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void output::setOpacity(half opacity)
```

#### Discussion

This function customizes the alpha component of the rendered particle output, controlling its transparency. This affects only the rendered appearance and does not modify the particle node itself.

> **Note**: ![Graph](/images/com.apple.computegraph/output__setOpacity.svg)

## Parameters

- `opacity`: The opacity value (0.0 = fully transparent, 1.0 = fully opaque).


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/setopacity)*