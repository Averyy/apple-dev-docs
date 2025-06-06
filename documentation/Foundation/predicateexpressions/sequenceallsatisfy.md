# PredicateExpressions.SequenceAllSatisfy

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
struct SequenceAllSatisfy<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Topics

### Initializers
- [init(LHS, builder: (PredicateExpressions.Variable<PredicateExpressions.SequenceAllSatisfy<LHS, RHS>.Element>) -> RHS)](predicateexpressions/sequenceallsatisfy/init(_:builder:).md)
### Instance Properties
- [let sequence: LHS](predicateexpressions/sequenceallsatisfy/sequence.md)
- [let test: RHS](predicateexpressions/sequenceallsatisfy/test.md)
- [let variable: PredicateExpressions.Variable<PredicateExpressions.SequenceAllSatisfy<LHS, RHS>.Element>](predicateexpressions/sequenceallsatisfy/variable.md)
### Type Aliases
- [PredicateExpressions.SequenceAllSatisfy.Element](predicateexpressions/sequenceallsatisfy/element.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/sequenceallsatisfy)*