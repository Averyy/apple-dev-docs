---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccompactedsequence/map(_:)-1ja6u"
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
func map<Transformed>(_ transform: @escaping @Sendable (Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccompactedsequence/map(_:)-1ja6u)*