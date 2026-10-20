# PredicateExpressions.Arithmetic

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(lhs: LHS, rhs: RHS, op: PredicateExpressions.ArithmeticOperator)](./arithmetic/init%28lhs,rhs,op%29.md)
### Instance Properties
- [let lhs: LHS](./arithmetic/lhs.md)
- [let op: PredicateExpressions.ArithmeticOperator](./arithmetic/op.md)
- [let rhs: RHS](./arithmetic/rhs.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/arithmetic)*