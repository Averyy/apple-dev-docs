# PredicateExpressions.Filter

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
struct Filter<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Topics

### Initializers
- [init(LHS, (PredicateExpressions.Variable<PredicateExpressions.Filter<LHS, RHS>.Element>) -> RHS)](./filter/init%28_,_%29.md)
### Instance Properties
- [let filter: RHS](./filter/filter.md)
- [let sequence: LHS](./filter/sequence.md)
- [let variable: PredicateExpressions.Variable<PredicateExpressions.Filter<LHS, RHS>.Element>](./filter/variable.md)
### Type Aliases
- [PredicateExpressions.Filter.Element](./filter/element.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/filter)*