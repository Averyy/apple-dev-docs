---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerationComponents

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Optional behavioral components that augment [`GenerateParameters`](./generateparameters.md) for a generation.

## Declaration

```swift
struct GenerationComponents
```

#### Overview

[`GenerateParameters`](./generateparameters.md) is a plain, `Sendable` value describing *what* to generate (sampling temperature, penalties, token limits, …). `GenerationComponents` carries the *behavioral* hooks that shape generation but are not themselves simple values – for example a custom [`LogitProcessor`](./logitprocessor.md) or parameter validation. Keeping these out of [`GenerateParameters`](./generateparameters.md) lets that type stay a pure value while still letting callers inject custom behavior through the same parameters-driven APIs ([`TokenIterator`](./tokeniterator.md), [`ChatSession`](./chatsession.md), the speculative iterators and the `generate(...)` free functions).

Every field is optional and defaulted, so an empty `GenerationComponents()` reproduces the default behavior and can be threaded through any entry point without changing existing results.

```swift
let components = GenerationComponents().appendingLogitProcessor {
    GrammarProcessor(grammar: grammar)
}
let session = ChatSession(model, components: components)
```

## Topics

### Initializers
- [init(logitProcessorFactory: (@Sendable () -> any LogitProcessor)?, parameterValidator: (@Sendable (GenerateParameters) throws -> Void)?)](./generationcomponents/init%28logitprocessorfactory,parametervalidator%29.md)
### Instance Properties
- [var logitProcessorFactory: (@Sendable () -> any LogitProcessor)?](./generationcomponents/logitprocessorfactory.md)
  Optional factory producing a custom [`LogitProcessor`](./logitprocessor.md) that is composed after the built-in penalty processor, see [`logitProcessor(parameters:)`](./generationcomponents/logitprocessor%28parameters%29.md).
- [var parameterValidator: (@Sendable (GenerateParameters) throws -> Void)?](./generationcomponents/parametervalidator.md)
  Optional validation for constraints that depend on generation parameters.
### Instance Methods
- [func appendingLogitProcessor(@Sendable () -> any LogitProcessor) -> GenerationComponents](./generationcomponents/appendinglogitprocessor%28_%29.md)
  Return a copy with another custom [`LogitProcessor`](./logitprocessor.md) appended.
- [func appendingParameterValidator(@Sendable (GenerateParameters) throws -> Void) -> GenerationComponents](./generationcomponents/appendingparametervalidator%28_%29.md)
  Return a copy with an additional generation-parameter validator.
- [func applyingThinkingBudget(ThinkingBudgetConfiguration, reasoning: ReasoningConfig, tokenizer: any Tokenizer, diagnosticHandler: (@Sendable (ThinkingBudgetDiagnostic) -> Void)?) throws -> GenerationComponents](./generationcomponents/applyingthinkingbudget%28_,reasoning,tokenizer,diagnostichandler%29.md)
  Return a copy that enforces a reasoning-token budget for every generation.
- [func logitProcessor(parameters: GenerateParameters) -> LogitProcessor?](./generationcomponents/logitprocessor%28parameters%29.md)
  Build the [`LogitProcessor`](./logitprocessor.md) for a single generation.
- [func logitProcessor(parameters: GenerateParameters, model: any LanguageModel) -> LogitProcessor?](./generationcomponents/logitprocessor%28parameters,model%29.md)
  As [`logitProcessor(parameters:)`](./generationcomponents/logitprocessor%28parameters%29.md), additionally masking the token ids the model suppresses – declared through [`SuppressedTokensProviding`](./suppressedtokensproviding.md) or read from its `generation_config.json`.
- [func validate(parameters: GenerateParameters) throws](./generationcomponents/validate%28parameters%29.md)
  Validate generation parameters for every configured component.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents)*