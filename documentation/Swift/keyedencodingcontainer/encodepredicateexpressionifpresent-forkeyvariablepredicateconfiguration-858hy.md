# encodePredicateExpressionIfPresent(_:forKey:variable:predicateConfiguration:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
mutating func encodePredicateExpressionIfPresent<T, each Input>(_ expression: T?, forKey key: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws where T : PredicateExpression, T : Encodable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodepredicateexpressionifpresent(_:forkey:variable:predicateconfiguration:)-858hy)*