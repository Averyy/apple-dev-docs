---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunking-swift.enum/remainder"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PrefillParameters.Chunking.remainder

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Legacy stride: chunks of exactly the step size. An escape hatch back to each model’s pre-[`PrefillParameters.Chunking.balanced`](./balanced.md) chunk boundaries and their exact outputs — on the default `LLMModel` path the remainder rides along with the `TokenIterator`’s first forward; models that reserve one position for the logits keep that shape and stride the rest.

## Declaration

```swift
case remainder
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunking-swift.enum/remainder)*