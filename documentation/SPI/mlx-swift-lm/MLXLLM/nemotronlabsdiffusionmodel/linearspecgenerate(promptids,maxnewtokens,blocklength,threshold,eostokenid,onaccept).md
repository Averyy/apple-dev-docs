---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/linearspecgenerate(promptids:maxnewtokens:blocklength:threshold:eostokenid:onaccept:)"
framework: "mlx-swift-lm/MLXLLM"
---

# linearSpecGenerate(promptIds:maxNewTokens:blockLength:threshold:eosTokenId:onAccept:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Linear speculative decoding: bidirectional drafter + AR verifier with a shared KV cache. Mirrors `linear_spec_generate(...)`.

## Declaration

```swift
func linearSpecGenerate(promptIds: [Int], maxNewTokens: Int = 128, blockLength: Int = 32, threshold: Float = 0.0, eosTokenId: Int? = nil, onAccept: ((_ tokens: [Int], _ nfe: Int) -> Void)? = nil) -> (tokens: [Int], nfe: Int)
```

## Discussion

Requires `batch_size == 1`. The drafter runs with bidirectional attention (no KV-cache update) over a `blockLength`-token block; the verifier runs the same block causally and **does** update the cache. Accepted tokens are the longest matching prefix (plus one bonus AR token), and the cache is trimmed to length to discard rejected tokens.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/linearspecgenerate(promptids:maxnewtokens:blocklength:threshold:eostokenid:onaccept:))*