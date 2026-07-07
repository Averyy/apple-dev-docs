# module::debug::drawVector

**Framework**: Compute Graph  
**Kind**: func

Draws a debug vector at the current element’s position.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void module::debug::drawVector(float3 vector, float scale, half4 color)
```

#### Discussion

Debug Lines are not enabled by default. You enable them in your editor or by setting `LinkOptions/debugDraw` to true when compiling your pipelines, and assigning a `DebugLinesProvider` to your ComputeGraphSimulation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/3d8d433a93fa76b140803d2b742b96c2/module__debug__drawVector.svg)

## Parameters

- `vector`: Direction of vector
- `scale`: Length of vector. Minimum is 0.01, which corresponds to 10cm.
- `color`: Color of line


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/module/debug/drawvector)*