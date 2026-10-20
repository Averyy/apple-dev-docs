# PredicateExpressions.SequenceAllSatisfy

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
struct SequenceAllSatisfy<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Topics

### Initializers
- [init(LHS, builder: (PredicateExpressions.Variable<PredicateExpressions.SequenceAllSatisfy<LHS, RHS>.Element>) -> RHS)](./sequenceallsatisfy/init%28_,builder%29.md)
### Instance Properties
- [let sequence: LHS](./sequenceallsatisfy/sequence.md)
- [let test: RHS](./sequenceallsatisfy/test.md)
- [let variable: PredicateExpressions.Variable<PredicateExpressions.SequenceAllSatisfy<LHS, RHS>.Element>](./sequenceallsatisfy/variable.md)
### Type Aliases
- [PredicateExpressions.SequenceAllSatisfy.Element](./sequenceallsatisfy/element.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/sequenceallsatisfy)*