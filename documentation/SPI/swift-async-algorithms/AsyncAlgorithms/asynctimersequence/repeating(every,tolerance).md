---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/repeating(every:tolerance:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# repeating(every:tolerance:)

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
static func repeating(every interval: Duration, tolerance: Duration? = nil) -> AsyncTimerSequence<SuspendingClock>
```

Available when `C` is `SuspendingClock`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/repeating(every:tolerance:))*