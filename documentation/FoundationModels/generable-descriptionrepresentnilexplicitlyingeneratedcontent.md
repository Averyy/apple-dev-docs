# Generable(description:representNilExplicitlyInGeneratedContent:)

**Framework**: Foundation Models  
**Kind**: macro

Conforms a type to [`Generable`](generable.md) protocol.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@attached
(extension, conformances: Generable, names: named(init(_:)), named(generatedContent)) @attached(member, names: arbitrary) macro Generable(description: String? = nil, representNilExplicitlyInGeneratedContent: Bool)
```

#### Overview

You can apply this macro to structures and enumerations.

```swift
@Generable(representNilExplicitlyInGeneratedContent: true)
struct Character {
  @Guide(description: "A short title")
  let title: String

  @Guide(description: "An optional short subtitle for the novel")
  let subtitle: String?

  @Guide(description: "The genre of the novel")
  let genre: Genre
}

@Generable
enum Genre {
  case fiction
  case nonFiction
}
```

The `representNilExplicitlyInGeneratedContent` argument controls how the model represents nil properties. When `false`, the model will omit nil properties from the generated content, so no property will be present. When `true`, the model will produce a property, but its value will be [`GeneratedContent.Kind.null`](generatedcontent/kind-swift.enum/null.md).

```swift
// representNilExplicitlyInGeneratedContent: false
let content = GeneratedContent(properties: [:])

// representNilExplicitlyInGeneratedContent: true
let content = GeneratedContent(properties: ["foo": nil])
```

Controlling this behavior can be important when interfacing with external systems, using custom adapters, or working with one-shot examples that contain explicitly encoded nils.

> **Note**: @Generable macro [`Generable(description:)`](generable(description:).md)

## See Also

- [macro Generable(description: String?)](generable(description:).md)
  Conforms a type to [`Generable`](generable.md) protocol.
- [macro Generable(name: String, description: String?, representNilExplicitlyInGeneratedContent: Bool)](generable(name:description:representnilexplicitlyingeneratedcontent:).md)
  Conforms a type to [`Generable`](generable.md) protocol, using a custom name for the schema instead of the Swift type name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generable(description:representnilexplicitlyingeneratedcontent:))*