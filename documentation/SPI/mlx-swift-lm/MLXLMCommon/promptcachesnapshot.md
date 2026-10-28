---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/promptcachesnapshot"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PromptCacheSnapshot

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A prompt cache and the model state that belongs with it.

## Declaration

```swift
struct PromptCacheSnapshot
```

## Overview

Keeping the two together is the point: a KV cache restored without its model state positions later tokens as if the cached prefix contained no images, which changes the output silently. Pass a snapshot to a `ChatSession` initializer that accepts a `promptCache` rather than unpacking it into the `cache:` initializer.

A snapshot does not carry the chat transcript. A `ChatSession` restored from one appends each new message rather than re-rendering the conversation, so a later image-bearing turn builds a different prompt than it would in a session that still holds its history. Positions stay correct either way. On vision encoders that attend across image boundaries (Qwen2-VL today) the new image’s features differ too, since it is encoded alone rather than beside the cached one; Qwen2.5-VL, Qwen3-VL, and GLM-OCR isolate each image and are unaffected.

The cache instances are mutable reference types. Transfer a snapshot to one session or copy the caches before constructing multiple sessions from it.

## Topics

### Initializers
- [init(cache: [KVCache], metadata: [String : String], state: LMOutput.State?)](./promptcachesnapshot/init%28cache,metadata,state%29.md)
  Pair a cache with the model state that belongs with it.
### Instance Properties
- [let cache: [KVCache]](./promptcachesnapshot/cache.md)
- [let metadata: [String : String]](./promptcachesnapshot/metadata.md)
- [let state: LMOutput.State?](./promptcachesnapshot/state.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/promptcachesnapshot)*