---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/preparedinputsplitting"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PreparedInputSplitting

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A model that can split its own prepared input at a token boundary, keeping only the media whose placeholders fall in the suffix.

## Declaration

```swift
protocol PreparedInputSplitting
```

#### Overview

Conform only if the media encoder computes each item’s features independently of the others; otherwise dropping cached items changes the features of the items that remain. `Qwen25VL` masks each frame to itself and conforms; `Qwen2VL` attends across the whole buffer and does not.

## Topics

### Instance Methods
- [func splitPreparedInput(LMInput, droppingFirst: Int) -> LMInput?](./preparedinputsplitting/splitpreparedinput%28_,droppingfirst%29.md)
  Return the suffix of `input` that begins at `prefixTokenCount`, carrying only the media whose placeholder tokens lie inside that suffix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/preparedinputsplitting)*