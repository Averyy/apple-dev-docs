# build_max(_:)

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
static func build_max<Elements>(_ elements: Elements) -> PredicateExpressions.SequenceMaximum<Elements> where Elements : PredicateExpression, Elements.Output : Sequence, Elements.Output.Element : Comparable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_max(_:))*