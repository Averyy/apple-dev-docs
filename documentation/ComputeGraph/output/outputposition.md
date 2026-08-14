# output::outputPosition

**Framework**: Compute Graph  
**Kind**: func

Returns the position of the rendered output.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float3 output::outputPosition()
```

#### Return Value

The 3D position of the rendered output in the graph’s local coordinate system.

#### Discussion

This function retrieves the 3D position where the particle will be rendered, which may differ from the particle node’s actual position if output transformations have been applied.

> **Note**: ![Graph](/images/com.apple.computegraph/output__outputPosition.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/outputposition)*