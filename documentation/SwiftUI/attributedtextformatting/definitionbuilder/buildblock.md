# buildBlock(_:_:)

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
static func buildBlock<F, each D>(_ first: F, _ definition: repeat each D) -> AttributedTextFormatting.TupleDefinition<F.Scope, F, repeat each D> where F : AttributedTextFormattingDefinition, repeat each D : AttributedTextFormattingDefinition
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder/buildblock(_:_:))*