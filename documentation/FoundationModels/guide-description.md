# Guide(description:_:)

**Framework**: Foundation Models  
**Kind**: macro

Allows for influencing the allowed values of properties of a [`Generable`](generable.md) type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@attached
(peer) macro Guide<RegexOutput>(description: String? = nil, _ guides: Regex<RegexOutput>)
```

#### Overview

> **Note**: `@Generable` macro [`Generable(description:)`](generable(description:).md)

## See Also

- [macro Guide(description: String)](guide(description:).md)
  Allows for influencing the allowed values of properties of a [`Generable`](generable.md) type.
- [struct GenerationGuide](generationguide.md)
  Guides that control how values are generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/guide(description:_:))*