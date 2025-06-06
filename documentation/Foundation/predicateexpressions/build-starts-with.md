# build_starts(_:with:)

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
static func build_starts<Base, Prefix>(_ base: Base, with prefix: Prefix) -> PredicateExpressions.SequenceStartsWith<Base, Prefix> where Base : PredicateExpression, Prefix : PredicateExpression, Base.Output : Sequence, Prefix.Output : Sequence, Base.Output.Element : Equatable, Base.Output.Element == Prefix.Output.Element
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_starts(_:with:))*