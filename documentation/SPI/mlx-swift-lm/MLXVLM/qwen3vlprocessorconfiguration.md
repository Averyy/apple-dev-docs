---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vlprocessorconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen3VLProcessorConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Qwen3VLProcessorConfiguration
```

## Topics

### Structures
- [Qwen3VLProcessorConfiguration.Size](./qwen3vlprocessorconfiguration/size-swift.struct.md)
  The synthesized min/max-pixel budget the processor consumes. Always resolved (non-optional) — see `var size`.
- [Qwen3VLProcessorConfiguration.SizeBudget](./qwen3vlprocessorconfiguration/sizebudget.md)
  The raw JSON `"size"` block. Newer Qwen3-VL configs (e.g. Qwen3.6-27B PARO) ship *only* `{longest_edge, shortest_edge}` — pixel-area budgets under the HF convention `shortest_edge → min_pixels`, `longest_edge → max_pixels` (same direct mapping GlmOcr uses); older configs ship `{min_pixels, max_pixels}`. Every field is optional so a config that omits any one still decodes: the processor loader swallows decode throws into a silent text-only fallback, so a hard requirement would make vision disappear instead of erroring.
### Initializers
- [init(from: any Decoder) throws](./qwen3vlprocessorconfiguration/init%28from%29.md)
### Instance Properties
- [let imageMean: [CGFloat]](./qwen3vlprocessorconfiguration/imagemean.md)
- [var imageMeanTuple: (CGFloat, CGFloat, CGFloat)](./qwen3vlprocessorconfiguration/imagemeantuple.md)
- [let imageProcessorType: String](./qwen3vlprocessorconfiguration/imageprocessortype.md)
- [let imageStd: [CGFloat]](./qwen3vlprocessorconfiguration/imagestd.md)
- [var imageStdTuple: (CGFloat, CGFloat, CGFloat)](./qwen3vlprocessorconfiguration/imagestdtuple.md)
- [var maxPixels: Int](./qwen3vlprocessorconfiguration/maxpixels.md)
- [let mergeSize: Int](./qwen3vlprocessorconfiguration/mergesize.md)
- [var minPixels: Int](./qwen3vlprocessorconfiguration/minpixels.md)
- [let patchSize: Int](./qwen3vlprocessorconfiguration/patchsize.md)
- [var size: Size](./qwen3vlprocessorconfiguration/size-swift.property.md)
- [let temporalPatchSize: Int](./qwen3vlprocessorconfiguration/temporalpatchsize.md)
### Default Implementations
- [Encodable Implementations](./qwen3vlprocessorconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen3vlprocessorconfiguration)*