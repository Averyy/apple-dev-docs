---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/argenerate(promptids:maxnewtokens:eostokenid:)"
framework: "mlx-swift-lm/MLXLLM"
---

# arGenerate(promptIds:maxNewTokens:eosTokenId:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Pure autoregressive generation (causal attention).

## Declaration

```swift
func arGenerate(promptIds: [Int], maxNewTokens: Int = 128, eosTokenId: Int? = nil) -> (tokens: [Int], nfe: Int)
```

#### Discussion

Mirrors `ar_generate` in `modeling_nemotron_labs_diffusion.py`. Returns the prompt concatenated with newly generated tokens, and the number of forward passes performed.

> **Note**: This method is provided for **symmetry** with [`diffusionGenerate(promptIds:maxNewTokens:blockLength:threshold:eosTokenId:onStep:)`](./diffusiongenerate%28promptids,maxnewtokens,blocklength,threshold,eostokenid,onstep%29.md) and [`linearSpecGenerate(promptIds:maxNewTokens:blockLength:threshold:eosTokenId:onAccept:)`](./linearspecgenerate%28promptids,maxnewtokens,blocklength,threshold,eostokenid,onaccept%29.md) so callers can pick a mode by method name. For real applications prefer driving AR generation through the standard pipeline (`ChatSession` / `ModelContainer.generate(...)`), which calls [`callAsFunction(_:cache:)`](./callasfunction%28_,cache%29.md) token-by-token via `TokenIterator` and adds streaming, temperature / top-p / repetition-penalty sampling, chunked prompt prefill, sliding-window and quantized KV caches, and wired-memory ticket coordination — none of which this method does.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/argenerate(promptids:maxnewtokens:eostokenid:))*