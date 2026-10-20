# init(_:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a prompt from the content of a builder closure.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(@PromptBuilder _ content: () throws -> Prompt) rethrows
```

**Other overloads**:

```swift
init(_ content: some PromptRepresentable)
```

## Parameters

- `content`: A closure that produces the prompt to send to the model.

## See Also

### Creating a prompt
- [struct PromptBuilder](../promptbuilder.md)
  A type that represents a prompt builder.
- [protocol PromptRepresentable](../promptrepresentable.md)
  A type whose value can represent a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/prompt/init(_:))*