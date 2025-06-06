# build_contains(_:_:)

**Framework**: Foundation  
**Kind**: method

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
static func build_contains<LHS, RHS>(_ lhs: LHS, _ rhs: RHS) -> PredicateExpressions.SequenceContains<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output : Equatable, RHS.Output == LHS.Output.Element
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-9bwzx)*