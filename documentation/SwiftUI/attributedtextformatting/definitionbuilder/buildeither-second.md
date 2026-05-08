# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where Scope == T.Scope, T : AttributedTextFormattingDefinition, F : AttributedTextFormattingDefinition, T.Scope == F.Scope
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder/buildeither(second:))*