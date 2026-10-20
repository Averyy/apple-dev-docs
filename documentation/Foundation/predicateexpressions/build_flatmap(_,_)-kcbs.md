# build_flatMap(_:_:)

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
static func build_flatMap<LHS, RHS, Wrapped, Result>(_ wrapped: LHS, _ builder: (PredicateExpressions.Variable<Wrapped>) -> RHS) -> PredicateExpressions.OptionalFlatMap<LHS, Wrapped, RHS, Result> where LHS : PredicateExpression, RHS : PredicateExpression, Result == RHS.Output, LHS.Output == Wrapped?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_flatmap(_:_:)-kcbs)*