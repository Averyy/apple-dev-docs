---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence/prefix(while:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# prefix(while:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.prefix(while:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func prefix(while predicate: @escaping @Sendable (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence/prefix(while:))*