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
static func build_subscript<Wrapped, Index>(_ wrapped: Wrapped, _ index: Index) -> PredicateExpressions.CollectionIndexSubscript<Wrapped, Index> where Wrapped : PredicateExpression, Index : PredicateExpression, Wrapped.Output : Collection, Index.Output == Wrapped.Output.Index
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:)-are7)*