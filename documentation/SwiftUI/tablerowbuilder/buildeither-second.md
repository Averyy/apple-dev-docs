# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method

Creates a row result for the second of two row content alternatives.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where Value == T.TableRowValue, T : TableRowContent, F : TableRowContent, T.TableRowValue == F.TableRowValue
```

#### Discussion

This method provides support for “if” statements in multi-statement closures, producing conditional content for the “else” branch.

## See Also

- [static func buildIf<C>(C?) -> C?](tablerowbuilder/buildif(_:).md)
  Creates a row result for conditional statements.
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(first:).md)
  Creates a row result for the first of two row content alternatives.
- [static func buildExpression<Content>(Content) -> Content](tablerowbuilder/buildexpression(_:).md)
  Builds an expression within the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildeither(second:))*