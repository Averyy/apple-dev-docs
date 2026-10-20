# PredicateExpressions.OptionalFlatMap

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
struct OptionalFlatMap<LHS, Wrapped, RHS, Result> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output == Wrapped?
```

## Topics

### Initializers
- [init(LHS, (PredicateExpressions.Variable<Wrapped>) -> RHS)](./optionalflatmap/init%28_,_%29-3sqz7.md)
- [init(LHS, (PredicateExpressions.Variable<Wrapped>) -> RHS)](./optionalflatmap/init%28_,_%29-fnq2.md)
### Instance Properties
- [let transform: RHS](./optionalflatmap/transform.md)
- [let variable: PredicateExpressions.Variable<Wrapped>](./optionalflatmap/variable.md)
- [let wrapped: LHS](./optionalflatmap/wrapped.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/optionalflatmap)*