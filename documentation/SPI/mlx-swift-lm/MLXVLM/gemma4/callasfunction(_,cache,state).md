---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4/callasfunction(_:cache:state:)"
framework: "mlx-swift-lm/MLXVLM"
---

# callAsFunction(_:cache:state:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

MTP-aware `LanguageModel` entry point. Reads `mtpEmitFlagKey` from the incoming `state` and threads it through to `Gemma4TextLanguageModel`; the returned `LMOutput` carries `mtpLastHiddenStatesKey` and `mtpSharedKVStatesKey` populated when the flag is set, empty otherwise. Overrides the protocol-extension default at `LanguageModel` which would discard `state`.

## Declaration

```swift
func callAsFunction(_ input: LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4/callasfunction(_:cache:state:))*