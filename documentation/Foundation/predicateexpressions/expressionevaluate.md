# PredicateExpressions.ExpressionEvaluate

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(expression: Transformation, input: repeat each Input)](./expressionevaluate/init%28expression,input%29.md)
### Instance Properties
- [let expression: Transformation](./expressionevaluate/expression.md)
- [let input: (repeat each Input)](./expressionevaluate/input.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)
- [PredicateExpression](../predicateexpression.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [StandardPredicateExpression](../standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/expressionevaluate)*