# encodePredicateExpression(_:forKey:variable:predicateConfiguration:)

**Framework**: Swift  
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
mutating func encodePredicateExpression<T, each Input>(_ expression: T, forKey key: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws where T : PredicateExpression, T : Encodable, T.Output == Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodepredicateexpression(_:forkey:variable:predicateconfiguration:)-92gv8)*