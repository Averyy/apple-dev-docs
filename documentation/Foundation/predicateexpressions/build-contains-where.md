# build_contains(_:where:)

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
static func build_contains<LHS, RHS>(_ lhs: LHS, where builder: (PredicateExpressions.Variable<LHS.Output.Element>) -> RHS) -> PredicateExpressions.SequenceContainsWhere<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:where:))*