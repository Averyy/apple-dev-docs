---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelContainer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Container for models that guarantees single threaded access.

## Declaration

```swift
final class ModelContainer
```

#### Overview

Wrap models used by e.g. the UI in a ModelContainer. Callers can access the model and/or tokenizer (any values from the [`ModelContext`](./modelcontext.md)):

```swift
let messages = [["role": "user", "content": prompt]]
let promptTokens = try await modelContainer.perform { context in
    try context.tokenizer.applyChatTemplate(messages: messages)
}
```

or:

```swift
let userInput: UserInput
let result = await modelContainer.perform { context in
    let input = try await context.processor.prepare(input: userInput)
    return generate(
        input: input, parameters: generateParameters, context: context
    ) { tokens in
    ...
    }
}
```

## Topics

### Initializers
- [init(context: consuming ModelContext)](./modelcontainer/init%28context%29.md)
### Instance Properties
- [var configuration: ModelConfiguration](./modelcontainer/configuration.md)
- [var modelDirectory: URL](./modelcontainer/modeldirectory.md)
  The resolved local model directory for the loaded container.
- [var processor: UserInputProcessor](./modelcontainer/processor.md)
- [var tokenizer: Tokenizer](./modelcontainer/tokenizer.md)
- [var tokenizerDirectory: URL](./modelcontainer/tokenizerdirectory.md)
  The resolved local tokenizer directory for the loaded container.
### Instance Methods
- [func applyChatTemplate(messages: [[String : String]]) async throws -> [Int]](./modelcontainer/applychattemplate%28messages%29.md)
  Apply chat template to messages and return token IDs.
- [func cacheStatus(parameters: GenerateParameters?) async throws -> KVCacheStatus](./modelcontainer/cachestatus%28parameters%29.md)
  Authoritative planned cache status for the given generation parameters.
- [func decode(tokenIds: [Int]) async -> String](./modelcontainer/decode%28tokenids%29.md)
  Decode token IDs to a string.
- [func decode(tokens: [Int]) async -> String](./modelcontainer/decode%28tokens%29.md)
- [func encode(String) async -> [Int]](./modelcontainer/encode%28_%29.md)
  Encode a string to token IDs.
- [func generate(input: sending consuming LMInput, parameters: GenerateParameters, wiredMemoryTicket: WiredMemoryTicket?, tools: [[String : any Sendable]]?) async throws -> AsyncStream<Generation>](./modelcontainer/generate%28input,parameters,wiredmemoryticket,tools%29.md)
  Generate tokens from prepared input, returning an AsyncStream.
- [func perform<R>(@Sendable (ModelContext) async throws -> sending R) async rethrows -> sending R](./modelcontainer/perform%28_%29-629d0.md)
  Perform an action on the [`ModelContext`](./modelcontext.md). Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func perform<R>(@Sendable (any LanguageModel, Tokenizer) throws -> sending R) async rethrows -> sending R](./modelcontainer/perform%28_%29-8ri5.md)
  Perform an action on the model and/or tokenizer. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func perform<V, R>(nonSendable: consuming V, @Sendable (ModelContext, V) async throws -> R) async rethrows -> sending R](./modelcontainer/perform%28nonsendable,_%29.md)
  Perform an action on the [`ModelContext`](./modelcontext.md) with additional (non `Sendable`) context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func perform<V, R>(values: V, @Sendable (ModelContext, V) async throws -> R) async rethrows -> sending R](./modelcontainer/perform%28values,_%29-7wais.md)
  Perform an action on the [`ModelContext`](./modelcontext.md) with additional context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func perform<V, R>(values: V, @Sendable (any LanguageModel, Tokenizer, V) throws -> sending R) async rethrows -> sending R](./modelcontainer/perform%28values,_%29-9yn9t.md)
  Perform an action on the model and/or tokenizer with additional context values. Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.
- [func prepare(input: sending consuming UserInput) async throws -> sending LMInput](./modelcontainer/prepare%28input%29.md)
  Prepare user input for generation.
- [func update(@Sendable (inout ModelContext) -> Void) async](./modelcontainer/update%28_%29.md)
  Update the owned `ModelContext`.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer)*