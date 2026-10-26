---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedonprojectionsequence/chunked(by:into:)-1qwcz"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chunked(by:into:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type when an `AsyncTimerSequence` fires.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func chunked<C, Collected>(by timer: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>> where Self : Sendable, C : Clock, Collected : RangeReplaceableCollection, Self.Element : Sendable, Self.Element == Collected.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedonprojectionsequence/chunked(by:into:)-1qwcz)*