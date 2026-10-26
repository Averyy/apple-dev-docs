---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantregistration"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4AssistantRegistration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: enum  
**Role**: Enumeration

Registers the `gemma4_assistant` model type with the shared MTP drafter type registry.

## Declaration

```swift
enum Gemma4AssistantRegistration
```

#### Overview

Callers must invoke this once before loading a drafter (typically at app launch). Re-registration is idempotent — it overwrites the prior creator with the same one.

Async because `ModelTypeRegistry` is an `actor` — registration calls require `await`. A bootstrap pattern like the synchronous `LLMTypeRegistry.shared = .init(creators: [...])` is not possible here: the drafter implementation (`Gemma4AssistantDraftModel`) lives in MLXVLM, and importing it into MLXLMCommon’s `MTPDrafterTypeRegistry.shared` would form a circular dependency.

Usage:

```swift
await Gemma4AssistantRegistration.register()
// ... later, load a drafter via MTPDrafterModelFactory.shared ...
```

## Topics

### Type Methods
- [static func register() async](./gemma4assistantregistration/register%28%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantregistration)*