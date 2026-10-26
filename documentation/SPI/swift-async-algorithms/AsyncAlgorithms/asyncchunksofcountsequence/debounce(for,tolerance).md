---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/debounce(for:tolerance:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# debounce(for:tolerance:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that emits the latest element after a given quiescence period has elapsed.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func debounce(for interval: Duration, tolerance: Duration? = nil) -> AsyncDebounceSequence<Self, ContinuousClock> where Self : Sendable, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/debounce(for:tolerance:))*