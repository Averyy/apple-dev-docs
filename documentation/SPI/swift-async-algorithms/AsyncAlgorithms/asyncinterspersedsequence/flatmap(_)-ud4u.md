---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinterspersedsequence/flatmap(_:)-ud4u"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# flatMap(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.flatMap(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func flatMap<SegmentOfResult>(_ transform: @escaping @Sendable (Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult> where SegmentOfResult : AsyncSequence
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinterspersedsequence/flatmap(_:)-ud4u)*