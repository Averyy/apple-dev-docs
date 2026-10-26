---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vlprocessorconfiguration/sizebudget"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen3VLProcessorConfiguration.SizeBudget

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

The raw JSON `"size"` block. Newer Qwen3-VL configs (e.g. Qwen3.6-27B PARO) ship *only* `{longest_edge, shortest_edge}` — pixel-area budgets under the HF convention `shortest_edge → min_pixels`, `longest_edge → max_pixels` (same direct mapping GlmOcr uses); older configs ship `{min_pixels, max_pixels}`. Every field is optional so a config that omits any one still decodes: the processor loader swallows decode throws into a silent text-only fallback, so a hard requirement would make vision disappear instead of erroring.

## Declaration

```swift
struct SizeBudget
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./sizebudget/init%28from%29.md)
### Instance Properties
- [let longestEdge: Int?](./sizebudget/longestedge.md)
- [let maxPixels: Int?](./sizebudget/maxpixels.md)
- [let minPixels: Int?](./sizebudget/minpixels.md)
- [let shortestEdge: Int?](./sizebudget/shortestedge.md)
### Default Implementations
- [Encodable Implementations](./sizebudget/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vlprocessorconfiguration/sizebudget)*