# Guide(description:_:)

**Framework**: Foundation Models  
**Kind**: macro

Allows for influencing the allowed values of properties of a generable type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@attached
(peer) macro Guide<RegexOutput>(description: String? = nil, _ guides: Regex<RegexOutput>)
```

## See Also

- [macro Guide(description: String)](guide(description:).md)
  Allows for influencing the allowed values of properties of a generable type.
- [struct GenerationGuide](generationguide.md)
  Guides that control how values are generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/guide(description:_:))*