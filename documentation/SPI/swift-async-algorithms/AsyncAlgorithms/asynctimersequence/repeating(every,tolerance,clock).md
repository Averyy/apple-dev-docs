---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/repeating(every:tolerance:clock:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# repeating(every:tolerance:clock:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Type Method

Create an `AsyncTimerSequence` with a given repeating interval.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
static func repeating(every interval: C.Instant.Duration, tolerance: C.Instant.Duration? = nil, clock: C) -> AsyncTimerSequence<C>
```

Available when `C` conforms to `Clock`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/repeating(every:tolerance:clock:))*