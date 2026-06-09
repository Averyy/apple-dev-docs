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
- watchOS 27.0+ (Beta)

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

> **Note**: @Generable macro [`Generable(description:representNilExplicitlyInGeneratedContent:)`](generable(description:representnilexplicitlyingeneratedcontent:).md)

## See Also

- [macro Generable(description: String?, representNilExplicitlyInGeneratedContent: Bool)](generable(description:representnilexplicitlyingeneratedcontent:).md)
  Conforms a type to [`Generable`](generable.md) protocol.
- [macro Generable(name: String, description: String?, representNilExplicitlyInGeneratedContent: Bool)](generable(name:description:representnilexplicitlyingeneratedcontent:).md)
  Conforms a type to [`Generable`](generable.md) protocol, using a custom name for the schema instead of the Swift type name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(description:))*