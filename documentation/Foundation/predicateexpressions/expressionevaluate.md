# PredicateExpressions.ExpressionEvaluate

**Framework**: Foundation  
**Kind**: struct

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
struct ExpressionEvaluate<Transformation, each Input, Output> where Transformation : PredicateExpression, repeat each Input : PredicateExpression, Transformation.Output == Expression<repeat (each Input).Output, Output>
```

## Topics

### Initializers
- [init(expression: Transformation, input: repeat each Input)](predicateexpressions/expressionevaluate/init(expression:input:).md)
### Instance Properties
- [let expression: Transformation](predicateexpressions/expressionevaluate/expression.md)
- [let input: (repeat each Input)](predicateexpressions/expressionevaluate/input.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/expressionevaluate)*