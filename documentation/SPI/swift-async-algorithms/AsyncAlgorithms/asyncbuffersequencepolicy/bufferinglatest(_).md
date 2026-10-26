---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequencepolicy/bufferinglatest(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# bufferingLatest(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Type Method

A policy for buffering elements until the limit is reached. After the limit is reached and a new element is produced by the upstream, the oldest buffered element will be discarded. If the limit is zero then no buffering policy is applied.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static func bufferingLatest(_ limit: Int) -> AsyncBufferSequencePolicy
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequencepolicy/bufferinglatest(_:))*