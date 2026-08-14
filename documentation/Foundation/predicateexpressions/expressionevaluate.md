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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Escapable](../swift/escapable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/expressionevaluate)*