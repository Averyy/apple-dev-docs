# PredicateExpressions.SequenceContainsWhere

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
struct SequenceContainsWhere<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Topics

### Initializers
- [init(LHS, builder: (PredicateExpressions.Variable<PredicateExpressions.SequenceContainsWhere<LHS, RHS>.Element>) -> RHS)](predicateexpressions/sequencecontainswhere/init(_:builder:).md)
### Instance Properties
- [let sequence: LHS](predicateexpressions/sequencecontainswhere/sequence.md)
- [let test: RHS](predicateexpressions/sequencecontainswhere/test.md)
- [let variable: PredicateExpressions.Variable<PredicateExpressions.SequenceContainsWhere<LHS, RHS>.Element>](predicateexpressions/sequencecontainswhere/variable.md)
### Type Aliases
- [PredicateExpressions.SequenceContainsWhere.Element](predicateexpressions/sequencecontainswhere/element.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/sequencecontainswhere)*