# PredicateExpressions.Filter

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
struct Filter<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Topics

### Initializers
- [init(LHS, (PredicateExpressions.Variable<PredicateExpressions.Filter<LHS, RHS>.Element>) -> RHS)](predicateexpressions/filter/init(_:_:).md)
### Instance Properties
- [let filter: RHS](predicateexpressions/filter/filter.md)
- [let sequence: LHS](predicateexpressions/filter/sequence.md)
- [let variable: PredicateExpressions.Variable<PredicateExpressions.Filter<LHS, RHS>.Element>](predicateexpressions/filter/variable.md)
### Type Aliases
- [PredicateExpressions.Filter.Element](predicateexpressions/filter/element.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/filter)*