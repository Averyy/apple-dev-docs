---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer"
framework: "mlx-swift-lm/MLXEmbedders"
---

# EmbedderModelContainer

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

Container for embedder models that guarantees single threaded access.

## Declaration

```swift
final class EmbedderModelContainer
```

## Overview

Wrap models used by e.g. the UI in a ModelContainer. Callers can access the model and/or tokenizer (any values from the [`EmbedderModelContext`](./embeddermodelcontext.md)):

```swift
let resultEmbeddings = await modelContainer.perform { context in
    let tokenizer = context.tokenizer
    let encoded = inputs.map {
        tokenizer.encode(text: $0, addSpecialTokens: true)
    }
    ...
    let modelOutput = context.model(
        padded, positionIds: nil, tokenTypeIds: tokenTypes, attentionMask: mask)

    let result = context.pooling(
        modelOutput,
        normalize: true, applyLayerNorm: true
    )
    result.eval()
    return result.map { $0.asArray(Float.self) }
}
```

## Topics

### Initializers
- [init(context: consuming EmbedderModelContext)](./embeddermodelcontainer/init%28context%29.md)
### Instance Properties
- [var configuration: ModelConfiguration](./embeddermodelcontainer/configuration.md)
- [var modelDirectory: URL](./embeddermodelcontainer/modeldirectory.md)
  The resolved local model directory for the loaded container.
- [var poolingStrategy: Pooling.Strategy](./embeddermodelcontainer/poolingstrategy.md)
- [var tokenizer: Tokenizer](./embeddermodelcontainer/tokenizer.md)
- [var tokenizerDirectory: URL](./embeddermodelcontainer/tokenizerdirectory.md)
  The resolved local tokenizer directory for the loaded container.
### Instance Methods
- [func perform<R>(@Sendable (EmbeddingModel, Tokenizer, Pooling) async throws -> sending R) async rethrows -> sending R](./embeddermodelcontainer/perform%28_%29-37clz.md)
- [func perform<R>(@Sendable (EmbedderModelContext) async throws -> sending R) async rethrows -> sending R](./embeddermodelcontainer/perform%28_%29-52sj4.md)
  Perform an action on the [`EmbedderModelContext`](./embeddermodelcontext.md). Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func perform<V, R>(nonSendable: consuming V, @Sendable (EmbedderModelContext, V) async throws -> R) async rethrows -> sending R](./embeddermodelcontainer/perform%28nonsendable,_%29.md)
  Perform an action on the [`EmbedderModelContext`](./embeddermodelcontext.md) with additional (non `Sendable`) context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func update(@Sendable (inout EmbedderModelContext) -> Void) async](./embeddermodelcontainer/update%28_%29.md)
  Update the owned `EmbedderModelContext`.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelcontainer)*