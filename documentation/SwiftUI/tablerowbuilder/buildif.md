# buildIf(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a row result for conditional statements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static func buildIf<C>(_ content: C?) -> C? where Value == C.TableRowValue, C : TableRowContent
```

#### Discussion

This method provides support for “if” statements in multi-statement closures, producing an optional value that is visible only when the condition evaluates to `true`.

## See Also

- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(first:).md)
  Creates a row result for the first of two row content alternatives.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(second:).md)
  Creates a row result for the second of two row content alternatives.
- [static func buildExpression<Content>(Content) -> Content](tablerowbuilder/buildexpression(_:).md)
  Builds an expression within the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildif(_:))*