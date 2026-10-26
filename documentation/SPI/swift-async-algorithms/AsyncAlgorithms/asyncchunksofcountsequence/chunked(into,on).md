---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/chunked(into:on:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(into:on:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type on the uniqueness of a given subject.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Subject, Collected>(into: Collected.Type, on projection: @escaping @Sendable (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, Collected> where Subject : Equatable, Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/chunked(into:on:))*