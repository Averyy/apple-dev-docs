# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds an expression within the builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func buildExpression<Content>(_ content: Content) -> Content where Value == Content.TableRowValue, Content : TableRowContent
```

## See Also

- [static func buildIf<C>(C?) -> C?](tablerowbuilder/buildif(_:).md)
  Creates a row result for conditional statements.
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(first:).md)
  Creates a row result for the first of two row content alternatives.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(second:).md)
  Creates a row result for the second of two row content alternatives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildexpression(_:))*