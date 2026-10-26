---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/frompeft(directory:numlayers:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# fromPEFT(directory:numLayers:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Loads a PEFT-format LoRA adapter directory and returns a [`LoRAContainer`](../loracontainer.md) you can [`load(into:)`](./load%28into%29.md) on a model.

## Declaration

```swift
static func fromPEFT(directory: URL, numLayers: Int = 1024) throws -> LoRAContainer
```

#### Return Value

A [`LoRAContainer`](../loracontainer.md) ready to be loaded into any [`LoRAModel`](../loramodel.md)-conforming model.

#### Discussion

PEFT format (Hugging Face `peft` library):

```
adapter_config.json:
  {
    "peft_type": "LORA",
    "r": 128,
    "lora_alpha": 512,
    "target_modules": ["o_proj"],
    ...
  }
adapter_model.safetensors (one pair per target module per layer):
  base_model.model.<inner-path>.<target_module>.lora_A.weight  shape [r, in]
  base_model.model.<inner-path>.<target_module>.lora_B.weight  shape [out, r]
```

MLX-native format ([`LoRALinear`](../loralinear.md) / [`QLoRALinear`](../qloralinear.md)):

```
loraA: [in, r], loraB: [r, out], scale = lora_alpha / r
```

Conversion performed by this loader:

- Strip the leading `base_model.model.` prefix.
- Rename `.lora_A.weight` → `.lora_a`, `.lora_B.weight` → `.lora_b`.
- Transpose both tensors to match MLX’s `[in, r]` / `[r, out]` convention.
- Compute `scale = lora_alpha / r`.

> **Throws**: [`ModelAdapterError.unsupportedAdapterType(_:)`](../modeladaptererror/unsupportedadaptertype%28_%29.md) if the adapter is not LORA, or if `use_dora=true` is set.

## Parameters

- `directory`: Directory containing `adapter_config.json` and `adapter_model.safetensors`.
- `numLayers`: Apply the adapter to at most the last `numLayers` entries of the model’s `loraLayers`. Defaults to a large value so the suffix slice covers every layer; pass a smaller value to restrict adapters to only the upper N transformer blocks.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/frompeft(directory:numlayers:))*