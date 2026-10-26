---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinterspersedsequence/filter(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# filter(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.filter(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func filter(_ isIncluded: @escaping @Sendable (Self.Element) async -> Bool) -> AsyncFilterSequence<Self>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinterspersedsequence/filter(_:))*