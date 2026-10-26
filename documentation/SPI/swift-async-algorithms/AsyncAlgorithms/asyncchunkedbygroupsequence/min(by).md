---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedbygroupsequence/min(by:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# min(by:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.min(by:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@warn_unqualified_access
func min(by areInIncreasingOrder: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedbygroupsequence/min(by:))*