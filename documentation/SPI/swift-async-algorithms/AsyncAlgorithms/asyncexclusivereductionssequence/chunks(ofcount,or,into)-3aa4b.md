---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence/chunks(ofcount:or:into:)-3aa4b"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunks(ofCount:or:into:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type of a given count or when an `AsyncTimerSequence` fires.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func chunks<C, Collected>(ofCount count: Int, or timer: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>> where Self : Sendable, C : Clock, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence/chunks(ofcount:or:into:)-3aa4b)*