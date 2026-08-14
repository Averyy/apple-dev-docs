# PredicateExpressions.OptionalFlatMap

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
struct OptionalFlatMap<LHS, Wrapped, RHS, Result> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output == Wrapped?
```

## Topics

### Initializers
- [init(LHS, (PredicateExpressions.Variable<Wrapped>) -> RHS)](predicateexpressions/optionalflatmap/init(_:_:)-3sqz7.md)
- [init(LHS, (PredicateExpressions.Variable<Wrapped>) -> RHS)](predicateexpressions/optionalflatmap/init(_:_:)-fnq2.md)
### Instance Properties
- [let transform: RHS](predicateexpressions/optionalflatmap/transform.md)
- [let variable: PredicateExpressions.Variable<Wrapped>](predicateexpressions/optionalflatmap/variable.md)
- [let wrapped: LHS](predicateexpressions/optionalflatmap/wrapped.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/optionalflatmap)*