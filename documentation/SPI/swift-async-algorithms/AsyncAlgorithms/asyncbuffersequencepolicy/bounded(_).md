---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequencepolicy/bounded(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# bounded(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Type Method

A policy for buffering elements until the limit is reached. Then consumption of the upstream `AsyncSequence` will be paused until elements are consumed from the buffer. If the limit is zero then no buffering policy is applied.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static func bounded(_ limit: Int) -> AsyncBufferSequencePolicy
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequencepolicy/bounded(_:))*