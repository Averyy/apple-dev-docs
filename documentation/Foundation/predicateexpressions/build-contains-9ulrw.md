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
static func build_contains<RangeExpression, Element>(_ range: RangeExpression, _ element: Element) -> PredicateExpressions.RangeExpressionContains<RangeExpression, Element> where RangeExpression : PredicateExpression, Element : PredicateExpression, RangeExpression.Output : RangeExpression, Element.Output == RangeExpression.Output.Bound
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-9ulrw)*