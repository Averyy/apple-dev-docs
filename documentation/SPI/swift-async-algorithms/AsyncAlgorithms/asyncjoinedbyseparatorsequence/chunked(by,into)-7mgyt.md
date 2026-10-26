---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedbyseparatorsequence/chunked(by:into:)-7mgyt"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(by:into:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type when a signal `AsyncSequence` produces an element.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Signal, Collected>(by signal: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedbyseparatorsequence/chunked(by:into:)-7mgyt)*