# PromptRepresentable

**Framework**: Foundation Models  
**Kind**: protocol

A type whose value can represent a prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol PromptRepresentable
```

#### Overview

> ❗ **Important**: Conformance to this protocol is provided automatically by the `@Generable` macro, you should  override its implementations. Overriding may negatively impact runtime performance and cause bugs.

For types that are not [`Generable`](generable.md), you may provide your own implementation.

Experiment with different representations to find one that works well for your type. Generally, any format that is easily understandable to humans will work well for the model as well.

```swift
struct FamousHistoricalFigure: PromptRepresentable {
    var name: String
    var biggestAccomplishment: String

    var promptRepresentation: Prompt {
        """
        Famous Historical Figure:
        - name: \(name)
        - best known for: \(biggestAccomplishment)
        """
    }
}

let response = try await LanguageModelSession().respond {
    "Tell me more about..."
    FamousHistoricalFigure(
        name: "Albert Einstein",
        biggestAccomplishment: "Theory of Relativity"
    )
}
```

## Topics

### Getting the representation
- [var promptRepresentation: Prompt](promptrepresentable/promptrepresentation.md)
  An instance that represents a prompt.

## Relationships

### Inherited By
- [ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
- [Generable](generable.md)
### Conforming Types
- [GeneratedContent](generatedcontent.md)
- [Prompt](prompt.md)

## See Also

- [init(_:)](prompt/init(_:).md)
- [struct PromptBuilder](promptbuilder.md)
  A type that represents a prompt builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/promptrepresentable)*