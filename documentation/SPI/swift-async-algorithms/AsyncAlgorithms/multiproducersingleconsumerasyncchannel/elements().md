---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/elements()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# elements()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Converts the channel to an asynchronous sequence for consumption.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
consuming func elements() -> some Sendable & AsyncSequence<Element, Failure>
```

Available when `Failure` conforms to `Error`.

#### Discussion

> ❗ **Important**: The returned asynchronous sequence only supports a single iterator to be created and will fatal error at runtime on subsequent calls to `makeAsyncIterator`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/elements())*