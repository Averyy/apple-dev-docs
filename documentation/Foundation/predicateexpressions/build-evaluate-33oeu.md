# build_evaluate(_:_:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
static func build_evaluate<Transformation, each Input, Output>(_ expression: Transformation, _ input: repeat each Input) -> PredicateExpressions.ExpressionEvaluate<Transformation, repeat each Input, Output> where Transformation : PredicateExpression, repeat each Input : PredicateExpression, Transformation.Output == Expression<repeat (each Input).Output, Output>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_evaluate(_:_:)-33oeu)*