---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence/chunked(by:)-4xoav"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(by:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks when a signal `AsyncSequence` produces an element.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chunked<Signal>(by signal: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal> where Self : Sendable, Signal : Sendable, Signal : AsyncSequence, Self.Element : Sendable, Signal.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence/chunked(by:)-4xoav)*