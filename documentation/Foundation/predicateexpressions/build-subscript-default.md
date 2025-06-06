# build_subscript(_:_:default:)

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
static func build_subscript<Wrapped, Key, Default>(_ wrapped: Wrapped, _ key: Key, default: Default) -> PredicateExpressions.DictionaryKeyDefaultValueSubscript<Wrapped, Key, Default> where Wrapped : PredicateExpression, Key : PredicateExpression, Default : PredicateExpression, Wrapped.Output == [Key.Output : Default.Output], Key.Output : Hashable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_subscript(_:_:default:))*