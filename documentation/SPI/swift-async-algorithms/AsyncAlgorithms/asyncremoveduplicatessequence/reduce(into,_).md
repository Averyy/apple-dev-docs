---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence/reduce(into:_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# reduce(into:_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.reduce(into:_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reduce<Result>(into initialResult: Result, _ updateAccumulatingResult: (inout Result, Self.Element) async throws -> Void) async rethrows -> Result
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence/reduce(into:_:))*