# init(model:tools:instructions:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a session in a blank slate state with string-based instructions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], instructions: String? = nil)
```

**Other overloads**:

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws -> Instructions) rethrows
```

```swift
convenience init(model: SystemLanguageModel = .default, tools: [any Tool] = [], instructions: Instructions? = nil)
```

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], instructions: Instructions? = nil)
```

```swift
convenience init(model: some LanguageModel, tools: [any Tool] = [], instructions: String? = nil)
```

```swift
convenience init<Failure>(model: some LanguageModel, tools: [any Tool] = [], @InstructionsBuilder instructions: () throws(Failure) -> Instructions) throws(Failure) where Failure : Error
```

## Discussion

- Parameters

  - model: The language model to use for this session.
  - tools: Tools to make available to the model for this session.
  - instructions: Instructions that control the model’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:tools:instructions:)-2q75q)*