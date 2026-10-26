---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedlogitsmodel/margin-swift.enum"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedLogitsModel.Margin

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: enum  
**Role**: Enumeration

How far above a row’s maximum the scripted token goes.

## Declaration

```swift
enum Margin
```

## Topics

### Enumeration Cases
- [ScriptedLogitsModel.Margin.custom(_:)](./margin-swift.enum/custom%28_%29.md)
- [ScriptedLogitsModel.Margin.dominant](./margin-swift.enum/dominant.md)
  Large enough that samplers and penalties do not override the script.
- [ScriptedLogitsModel.Margin.plausible](./margin-swift.enum/plausible.md)
  Small: the script wins under greedy decoding, but masks and penalties can beat it.
### Instance Properties
- [var value: Float](./margin-swift.enum/value.md)
### Default Implementations
- [Equatable Implementations](./margin-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedlogitsmodel/margin-swift.enum)*