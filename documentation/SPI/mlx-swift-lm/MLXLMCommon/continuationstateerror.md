---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/continuationstateerror"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ContinuationStateError

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Errors thrown when a warm KV cache is continued without the model state it requires.

## Declaration

```swift
enum ContinuationStateError
```

#### Overview

Models that place tokens with M-RoPE (the Qwen vision families, GLM-OCR) keep a continuation anchor in [`LMOutput.State`](./lmoutput/state-swift.struct.md) alongside the KV cache. Continuing a warm cache without that anchor positions new tokens as if the cached prefix contained no images, silently changing the output rather than failing.

Save and restore the pair with `savePromptCache(url:cache:metadata:state:)` and `loadPromptCacheSnapshot(url:)`.

## Topics

### Enumeration Cases
- [ContinuationStateError.missingState(model:key:)](./continuationstateerror/missingstate%28model,key%29.md)
  A cache warmed to a non-zero offset was supplied without the state key the model needs.
- [ContinuationStateError.unsupportedBatchContinuation(model:)](./continuationstateerror/unsupportedbatchcontinuation%28model%29.md)
  A warm cache was supplied for a batched continuation, but this model carries a single position anchor.
### Instance Properties
- [var errorDescription: String?](./continuationstateerror/errordescription.md)
### Default Implementations
- [Equatable Implementations](./continuationstateerror/equatable-implementations.md)
- [Error Implementations](./continuationstateerror/error-implementations.md)
- [LocalizedError Implementations](./continuationstateerror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Equatable
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/continuationstateerror)*