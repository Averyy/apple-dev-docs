# build_ClosedRange(lower:upper:)

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
static func build_ClosedRange<LHS, RHS>(lower: LHS, upper: RHS) -> PredicateExpressions.ClosedRange<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Comparable, LHS.Output == RHS.Output
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_closedrange(lower:upper:))*