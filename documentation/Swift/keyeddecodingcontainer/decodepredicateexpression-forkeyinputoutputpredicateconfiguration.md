# decodePredicateExpression(forKey:input:output:predicateConfiguration:)

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
mutating func decodePredicateExpression<each Input, Output>(forKey key: KeyedDecodingContainer<K>.Key, input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decodepredicateexpression(forkey:input:output:predicateconfiguration:))*