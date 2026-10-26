---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccombinelatest3sequence/chunks(ofcount:or:into:)-1z3"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunks(ofCount:or:into:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type of a given count or when a signal `AsyncSequence` produces an element.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunks<Signal, Collected>(ofCount count: Int, or signal: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccombinelatest3sequence/chunks(ofcount:or:into:)-1z3)*