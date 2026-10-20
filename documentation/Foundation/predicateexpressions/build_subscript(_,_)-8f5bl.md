# build_subscript(_:_:)

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
static func build_subscript<Wrapped, Range>(_ wrapped: Wrapped, _ range: Range) -> PredicateExpressions.CollectionRangeSubscript<Wrapped, Range> where Wrapped : PredicateExpression, Range : PredicateExpression, Wrapped.Output : Collection, Range.Output == Range<Wrapped.Output.Index>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:)-8f5bl)*