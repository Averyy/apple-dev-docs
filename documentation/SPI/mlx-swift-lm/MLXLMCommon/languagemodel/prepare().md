---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/prepare()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prepare()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Build derived state after checkpoint or adapter topology updates and before the model is used for inference.

## Declaration

```swift
func prepare() throws
```

#### Discussion

Implementations may materialize arrays or replace storage-sharing module views. The library invokes this lifecycle hook while it has exclusive access to the model; inference calls must remain read-only.

## Default Implementations

### LanguageModel Implementations
- [func prepare() throws](./prepare%28%29-5ngae.md)
  Most language models have no derived inference state to prepare.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/prepare())*