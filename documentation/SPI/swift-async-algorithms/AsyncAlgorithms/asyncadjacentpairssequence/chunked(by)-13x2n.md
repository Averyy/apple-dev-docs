---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncadjacentpairssequence/chunked(by:)-13x2n"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(by:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks by testing if elements belong in the same group.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked(by belongInSameGroup: @escaping @Sendable (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, [Self.Element]>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncadjacentpairssequence/chunked(by:)-13x2n)*