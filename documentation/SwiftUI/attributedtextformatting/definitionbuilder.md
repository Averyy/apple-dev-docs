# AttributedTextFormatting.DefinitionBuilder

**Framework**: SwiftUI  
**Kind**: struct

A result builder for attributed text formatting definition.

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
@resultBuilder
struct DefinitionBuilder<Scope>
```

## Topics

### Type Methods
- [static func buildBlock<S>() -> AttributedTextFormatting.EmptyDefinition<S>](attributedtextformatting/definitionbuilder/buildblock.md)
- [static func buildBlock<D>(D) -> D](attributedtextformatting/definitionbuilder/buildblock(_:).md)
- [static func buildBlock<F, each D>(F, repeat each D) -> AttributedTextFormatting.TupleDefinition<F.Scope, F, repeat each D>](attributedtextformatting/definitionbuilder/buildblock(_:_:).md)
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](attributedtextformatting/definitionbuilder/buildeither(first:).md)
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](attributedtextformatting/definitionbuilder/buildeither(second:).md)
- [static func buildExpression<D>(D) -> D](attributedtextformatting/definitionbuilder/buildexpression(_:).md)
- [static func buildIf<D>(D?) -> D?](attributedtextformatting/definitionbuilder/buildif(_:).md)
- [static func buildLimitedAvailability<D>(D) -> AttributedTextFormatting.AnyDefinition<Scope>](attributedtextformatting/definitionbuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder)*