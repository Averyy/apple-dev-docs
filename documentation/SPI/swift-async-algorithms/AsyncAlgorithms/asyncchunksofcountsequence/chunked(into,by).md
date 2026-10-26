---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/chunked(into:by:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(into:by:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type by testing if elements belong in the same group.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Collected>(into: Collected.Type, by belongInSameGroup: @escaping @Sendable (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, Collected> where Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/chunked(into:by:))*