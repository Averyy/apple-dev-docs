---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence/map(_:)-20wy4"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# map(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.map(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func map<Transformed>(_ transform: @escaping @Sendable (Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence/map(_:)-20wy4)*