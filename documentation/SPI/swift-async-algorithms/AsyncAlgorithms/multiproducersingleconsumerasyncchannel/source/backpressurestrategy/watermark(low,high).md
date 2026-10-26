---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/backpressurestrategy/watermark(low:high:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# watermark(low:high:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Type Method

A backpressure strategy using a high and low watermark to suspend and resume production respectively.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func watermark(low: Int, high: Int) -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.BackpressureStrategy
```

## Parameters

- `low`: When the number of buffered elements drops below the low watermark, producers will be resumed.
- `high`: When the number of buffered elements rises above the high watermark, producers will be suspended.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/backpressurestrategy/watermark(low:high:))*