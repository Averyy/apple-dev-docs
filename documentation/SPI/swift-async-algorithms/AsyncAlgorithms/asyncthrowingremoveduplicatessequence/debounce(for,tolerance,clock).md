---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingremoveduplicatessequence/debounce(for:tolerance:clock:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# debounce(for:tolerance:clock:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that emits the latest element after a given quiescence period has elapsed by using a specified Clock.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func debounce<C>(for interval: C.Instant.Duration, tolerance: C.Instant.Duration? = nil, clock: C) -> AsyncDebounceSequence<Self, C> where Self : Sendable, C : Clock, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingremoveduplicatessequence/debounce(for:tolerance:clock:))*