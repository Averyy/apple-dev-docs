# PredicateExpressions.PredicateEvaluate

**Framework**: Foundation  
**Kind**: struct

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
- [init(predicate: Condition, input: repeat each Input)](predicateexpressions/predicateevaluate/init(predicate:input:).md)
### Instance Properties
- [let input: (repeat each Input)](predicateexpressions/predicateevaluate/input.md)
- [let predicate: Condition](predicateexpressions/predicateevaluate/predicate.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/predicateevaluate)*