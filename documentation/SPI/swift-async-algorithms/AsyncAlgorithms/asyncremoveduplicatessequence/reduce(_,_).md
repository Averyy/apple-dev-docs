---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence/reduce(_:_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# reduce(_:_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reduce(_:_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Self.Element) async throws -> Result) async rethrows -> Result
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence/reduce(_:_:))*