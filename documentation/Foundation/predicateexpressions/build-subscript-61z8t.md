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
static func build_subscript<Wrapped, Key, Value>(_ wrapped: Wrapped, _ key: Key) -> PredicateExpressions.DictionaryKeySubscript<Wrapped, Key, Value> where Wrapped : PredicateExpression, Key : PredicateExpression, Wrapped.Output == [Key.Output : Value], Key.Output : Hashable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:)-61z8t)*