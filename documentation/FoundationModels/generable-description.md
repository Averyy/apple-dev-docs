# Generable(description:)

**Framework**: Foundation Models  
**Kind**: macro

Conforms a type to [`Generable`](generable.md) protocol.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@attached
(extension, conformances: Generable, names: named(init(_:)), named(generatedContent)) @attached(member, names: arbitrary) macro Generable(description: String? = nil)
```

## Mentions

- [Generating Swift data structures with guided generation](generating-swift-data-structures-with-guided-generation.md)

#### Overview

You can apply this macro to structures and enumerations.

```swift
@Generable
struct NovelIdea {
  @Guide(description: "A short title")
  let title: String

  @Guide(description: "A short subtitle for the novel")
  let subtitle: String

  @Guide(description: "The genre of the novel")
  let genre: Genre
}

@Generable
enum Genre {
  case fiction
  case nonFiction
}
```

> **Note**: @Guide macro [`Guide(description:)`](guide(description:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(description:))*