---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel/compacted()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# compacted()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Returns a new `AsyncSequence` that iterates over every non-nil element from the original `AsyncSequence`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func compacted<Unwrapped>() -> AsyncCompactedSequence<Self, Unwrapped> where Self.Element == Unwrapped?
```

## Return Value

An `AsyncSequence` where the element is the unwrapped original element and iterates over every non-nil element from the original `AsyncSequence`.

## Discussion

Produces the same result as `c.compactMap { $0 }`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel/compacted())*