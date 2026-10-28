# init(model:tools:instructions:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a session with the model, tools, and instructions you provide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], instructions: Instructions? = nil)
```

**Other overloads**:

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws -> Instructions) rethrows
```

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], instructions: Instructions? = nil)
```

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], instructions: String? = nil)
```

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], instructions: String? = nil)
```

```swift
convenience init<Failure>(model: some LanguageModel, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws(Failure) -> Instructions) throws(Failure) where Failure : Error
```

## Parameters

- `model`: The language model the session uses to generate responses.
- `tools`: The tools the model can call while responding.
- `instructions`: The instructions that guide the model’s behavior for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:instructions:)-2vug)*