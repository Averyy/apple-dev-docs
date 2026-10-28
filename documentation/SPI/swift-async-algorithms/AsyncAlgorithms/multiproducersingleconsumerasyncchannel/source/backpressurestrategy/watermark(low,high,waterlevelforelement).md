---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/backpressurestrategy/watermark(low:high:waterlevelforelement:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# watermark(low:high:waterLevelForElement:)

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
static func watermark(low: Int, high: Int, waterLevelForElement: @escaping @Sendable (borrowing Element) -> Int) -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.BackpressureStrategy
```

## Discussion

> ❗ **Important**: `waterLevelForElement` will be called during a lock on each element when it is written into the source and when it is consumed from the channel, so it must be side-effect free and at best constant in time.

## Parameters

- `low`: When the number of buffered elements drops below the low watermark, producers will be resumed.
- `high`: When the number of buffered elements rises above the high watermark, producers will be suspended.
- `waterLevelForElement`: A closure used to compute the contribution of each buffered element to the current water level.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/backpressurestrategy/watermark(low:high:waterlevelforelement:))*