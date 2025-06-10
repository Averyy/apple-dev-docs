# PredicateExpressions.Arithmetic

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Arithmetic<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Numeric, LHS.Output == RHS.Output
```

## Topics

### Initializers
- [init(lhs: LHS, rhs: RHS, op: PredicateExpressions.ArithmeticOperator)](predicateexpressions/arithmetic/init(lhs:rhs:op:).md)
### Instance Properties
- [let lhs: LHS](predicateexpressions/arithmetic/lhs.md)
- [let op: PredicateExpressions.ArithmeticOperator](predicateexpressions/arithmetic/op.md)
- [let rhs: RHS](predicateexpressions/arithmetic/rhs.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/arithmetic)*