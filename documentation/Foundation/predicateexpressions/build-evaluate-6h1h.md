# build_evaluate(_:_:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
static func build_evaluate<Condition, each Input>(_ predicate: Condition, _ input: repeat each Input) -> PredicateExpressions.PredicateEvaluate<Condition, repeat each Input> where Condition : PredicateExpression, repeat each Input : PredicateExpression, Condition.Output == Predicate<repeat (each Input).Output>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_evaluate(_:_:)-6h1h)*