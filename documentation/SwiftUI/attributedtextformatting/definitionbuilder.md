# AttributedTextFormatting.DefinitionBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A result builder for attributed text formatting definition.

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
@resultBuilder
struct DefinitionBuilder<Scope>
```

## Topics

### Type Methods
- [static func buildBlock<S>() -> AttributedTextFormatting.EmptyDefinition<S>](./definitionbuilder/buildblock%28%29.md)
- [static func buildBlock<D>(D) -> D](./definitionbuilder/buildblock%28_%29.md)
- [static func buildBlock<F, each D>(F, repeat each D) -> AttributedTextFormatting.TupleDefinition<F.Scope, F, repeat each D>](./definitionbuilder/buildblock%28_,_%29.md)
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](./definitionbuilder/buildeither%28first%29.md)
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](./definitionbuilder/buildeither%28second%29.md)
- [static func buildExpression<D>(D) -> D](./definitionbuilder/buildexpression%28_%29.md)
- [static func buildIf<D>(D?) -> D?](./definitionbuilder/buildif%28_%29.md)
- [static func buildLimitedAvailability<D>(D) -> AttributedTextFormatting.AnyDefinition<Scope>](./definitionbuilder/buildlimitedavailability%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/definitionbuilder)*