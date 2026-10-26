---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedbyseparatorsequence/chunks(ofcount:into:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunks(ofCount:into:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` of a given count.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunks<Collected>(ofCount count: Int, into: Collected.Type) -> AsyncChunksOfCountSequence<Self, Collected> where Collected : RangeReplaceableCollection, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedbyseparatorsequence/chunks(ofcount:into:))*