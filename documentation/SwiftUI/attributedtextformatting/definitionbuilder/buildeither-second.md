# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where Scope == T.Scope, T : AttributedTextFormattingDefinition, F : AttributedTextFormattingDefinition, T.Scope == F.Scope
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder/buildeither(second:))*