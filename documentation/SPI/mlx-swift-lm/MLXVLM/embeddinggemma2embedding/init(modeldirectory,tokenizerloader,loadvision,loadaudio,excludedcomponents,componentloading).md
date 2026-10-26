---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/init(modeldirectory:tokenizerloader:loadvision:loadaudio:excludedcomponents:componentloading:)"
framework: "mlx-swift-lm/MLXVLM"
---

# init(modelDirectory:tokenizerLoader:loadVision:loadAudio:excludedComponents:componentLoading:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(modelDirectory: URL, tokenizerLoader: any TokenizerLoader, loadVision: Bool = true, loadAudio: Bool = true, excludedComponents: Set<ModelComponent> = [], componentLoading: ComponentLoading = .onFirstUse) async throws
```

## Parameters

- `modelDirectory`: A local `embedding_gemma2` checkpoint directory.
- `tokenizerLoader`: Loads the checkpoint’s tokenizer.
- `loadVision`: Allow image/video inputs; false excludes the vision component.
- `loadAudio`: Allow audio inputs; false excludes the audio component.
- `excludedComponents`: Components that must never load.
- `componentLoading`: Load encoders on first use, or immediately with the text model.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding/init(modeldirectory:tokenizerloader:loadvision:loadaudio:excludedcomponents:componentloading:))*