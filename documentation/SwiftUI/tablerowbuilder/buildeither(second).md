# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a row result for the second of two row content alternatives.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where Value == T.TableRowValue, T : TableRowContent, F : TableRowContent, T.TableRowValue == F.TableRowValue
```

Available when `Value` conforms to `Identifiable`.

#### Discussion

This method provides support for “if” statements in multi-statement closures, producing conditional content for the “else” branch.

## See Also

### Building a row from conditionals
- [static func buildIf<C>(C?) -> C?](./buildif%28_%29.md)
  Creates a row result for conditional statements.
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](./buildeither%28first%29.md)
  Creates a row result for the first of two row content alternatives.
- [static func buildExpression<Content>(Content) -> Content](./buildexpression%28_%29.md)
  Builds an expression within the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildeither(second:))*