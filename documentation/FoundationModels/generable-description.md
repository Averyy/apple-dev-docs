# Generable(description:)

**Framework**: Foundation Models  
**Kind**: macro

Conforms a type to generable.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(description:))*