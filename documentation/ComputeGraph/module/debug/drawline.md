# module::debug::drawLine

**Framework**: Compute Graph  
**Kind**: func

Draws a debug line

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void module::debug::drawLine(float3 from, float3 to, half4 color)
```

#### Discussion

Debug Lines are not enabled by default. You enable them in your editor or by setting `LinkOptions/debugDraw` to true when compiling your pipelines, and assigning a `DebugLinesProvider` to your ComputeGraphSimulation.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/ca32ee225df05e4cb96dd64e93a0356b/module__debug__drawLine.svg)

## Parameters

- `from`: Start of line
- `to`: End of line
- `color`: Color of line


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/module/debug/drawline)*