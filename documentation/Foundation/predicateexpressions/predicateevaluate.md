# PredicateExpressions.PredicateEvaluate

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
struct PredicateEvaluate<Condition, each Input> where Condition : PredicateExpression, repeat each Input : PredicateExpression, Condition.Output == Predicate<repeat (each Input).Output>
```

## Topics

### Initializers
- [init(predicate: Condition, input: repeat each Input)](./predicateevaluate/init%28predicate,input%29.md)
### Instance Properties
- [let input: (repeat each Input)](./predicateevaluate/input.md)
- [let predicate: Condition](./predicateevaluate/predicate.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/predicateevaluate)*