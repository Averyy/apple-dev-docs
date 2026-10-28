---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding"
framework: "mlx-swift-lm/MLXVLM"
---

# EmbeddingGemma2Embedding

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Embeddings of text, images, video and audio from an EmbeddingGemma 2 checkpoint, in one shared space. Load the checkpoint once and reuse this actor for every call.

## Declaration

```swift
actor EmbeddingGemma2Embedding
```

## Overview

```swift
let embeddings = try await EmbeddingGemma2Embedding(
    modelDirectory: directory, tokenizerLoader: loader)
let query = try await embeddings.embed(
    .init(text: "What causes the northern lights?"), task: .searchQuery)
let clip = try await embeddings.embed(
    .init([.text("Aurora over Tromsø: "), .video(.url(movie)), .audio(.url(narration))]),
    task: .document)
```

## Topics

### Structures
- [EmbeddingGemma2Embedding.Input](./embeddinggemma2embedding/input.md)
  One independently embedded item: text and media in reading order.
### Initializers
- [init(modelDirectory: URL, tokenizerLoader: any TokenizerLoader, loadVision: Bool, loadAudio: Bool, excludedComponents: Set<ModelComponent>, componentLoading: ComponentLoading) async throws](./embeddinggemma2embedding/init%28modeldirectory,tokenizerloader,loadvision,loadaudio,excludedcomponents,componentloading%29.md)
### Instance Properties
- [let supportedModalities: Set<Modality>](./embeddinggemma2embedding/supportedmodalities.md)
  Modalities declared by the checkpoint and allowed by the loading policy. Encoders and processors load on first use.
### Instance Methods
- [func embed(Input, task: Task, dimensions: Int?) async throws -> [Float]](./embeddinggemma2embedding/embed%28_,task,dimensions%29-3gymw.md)
  Embeds one item; returns a unit-length float32 vector.
- [func embed([Input], task: Task, dimensions: Int?) async throws -> [[Float]]](./embeddinggemma2embedding/embed%28_,task,dimensions%29-9m6eh.md)
  Embeds independent items in input order, one at a time to bound working memory. Retrieval uses `.searchQuery` for queries and `.document` for corpus items.
### Type Methods
- [static func prompt(text: String, title: String?, task: Task) -> String](./embeddinggemma2embedding/prompt%28text,title,task%29.md)
  The task instruction prefix from the model card. Inputs that already carry one pass through unchanged.
### Enumerations
- [EmbeddingGemma2Embedding.Error](./embeddinggemma2embedding/error.md)
- [EmbeddingGemma2Embedding.Modality](./embeddinggemma2embedding/modality.md)
  Input kinds accepted by this loaded checkpoint.
- [EmbeddingGemma2Embedding.Task](./embeddinggemma2embedding/task.md)
  The task an embedding is prepared for. Use `.searchQuery` for queries and `.document` for corpus items; compared items must share a task’s space.
### Default Implementations
- [Actor Implementations](./embeddinggemma2embedding/actor-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.Actor


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/embeddinggemma2embedding)*