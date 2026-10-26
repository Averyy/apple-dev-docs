---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/foreachchunk(total:reserving:defaultstepsize:maximumstepsize:_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# forEachChunk(total:reserving:defaultStepSize:maximumStepSize:_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Drives a chunked prefill over `total` positions and returns the number of positions processed.

## Declaration

```swift
func forEachChunk(total: Int, reserving: Int = 1, defaultStepSize: Int = PrefillParameters.defaultStepSize, maximumStepSize: Int? = nil, _ body: (Range<Int>) -> Void) throws -> Int
```

#### Discussion

Computes the chunk length once, then calls `body` with each chunk’s range. The driver owns the loop’s shared obligations: cooperative cancellation between chunks (a long prompt must be interruptible — see the note in `LLMModel.prepare`), an autorelease pool per chunk (long prompts run hundreds of forwards before any autorelease boundary), the per-chunk [`progress`](./progress.md) report, and clearing the MLX buffer cache after each chunk, as mlx-lm does. The KV cache grows with every chunk, so the buffers it outgrows cannot be reused and would otherwise stay in the buffer cache. `body` performs the model’s forward and its own cache fencing (`asyncEval`/`eval`).

`reserving` positions are left unprocessed for the caller’s final forward — the one that produces logits (1 for every current caller). Under [`PrefillParameters.Chunking.unchunked`](./chunking-swift.enum/unchunked.md) no chunking happens and 0 is returned: the caller’s final forward takes the whole prompt.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/foreachchunk(total:reserving:defaultstepsize:maximumstepsize:_:))*