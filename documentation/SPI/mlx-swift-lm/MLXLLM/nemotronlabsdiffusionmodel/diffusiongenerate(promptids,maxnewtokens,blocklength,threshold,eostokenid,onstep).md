---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/diffusiongenerate(promptids:maxnewtokens:blocklength:threshold:eostokenid:onstep:)"
framework: "mlx-swift-lm/MLXLLM"
---

# diffusionGenerate(promptIds:maxNewTokens:blockLength:threshold:eosTokenId:onStep:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Block-wise diffusion (parallel) decoding.

## Declaration

```swift
func diffusionGenerate(promptIds: [Int], maxNewTokens: Int, blockLength: Int = 32, threshold: Float? = 0.9, eosTokenId: Int? = nil, onStep: ((_ tokens: [Int], _ nfe: Int) -> Void)? = nil) -> (tokens: [Int], nfe: Int)
```

#### Discussion

Mirrors `generate(...)` in `modeling_nemotron_labs_diffusion.py` with `causal_context = False`. The prompt is causally prefilled into a shared KV cache once. Each block of `blockLength` tokens is initialized to `mask_token_id` and refined in up to `blockLength` denoising steps: at each step the block is forwarded bidirectionally, attending against the cached prefix without re-running it. After each step the cache is trimmed by `blockLength` so the next step writes over the same slots. Once a block stabilizes, we run one causal forward over its finalized tokens to commit their K/V into the cache for subsequent blocks.

> **Design note — model-local rather than protocol-driven**: The block-wise denoising loop here (causal prefill → bidirectional block forward → cache-trim → confidence-driven commit → causal commit) is the standard mask-diffusion LM recipe and would generalize to other mask-diffusion models. A `DiffusionLanguageModel` protocol could in principle hoist this into a default extension, parameterized by a model-supplied `bidirectionalLogits(_:cache:)` and a `maskTokenId`.
>
> That generalization is intentionally not done now. Nemotron is the only mask-diffusion port in this repo, and several knobs here are model-specific: the bidirectional-vs-causal mode switch on the encoder is a Nemotron design, the threshold/top-N commit policy and the “fall back to single most-confident token” behavior are implementation choices, and `causal_context=False` is one of two paradigms the upstream Python exposes. Premature abstraction over a single example tends to encode whichever model arrived first.
>
> Re-visit when a second mask-diffusion model is added. With two implementations to compare, the right protocol shape (which knobs are common, which need policy-strategy hooks, what the bidirectional forward should look like generically) becomes obvious from the differences, and the abstraction pays for itself.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronlabsdiffusionmodel/diffusiongenerate(promptids:maxnewtokens:blocklength:threshold:eostokenid:onstep:))*