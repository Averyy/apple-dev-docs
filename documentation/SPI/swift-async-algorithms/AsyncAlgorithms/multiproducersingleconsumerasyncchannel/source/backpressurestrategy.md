---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/backpressurestrategy"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannel.Source.BackpressureStrategy

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A struct representing the backpressure of the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct BackpressureStrategy
```

## Topics

### Type Methods
- [static func watermark(low: Int, high: Int) -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.BackpressureStrategy](./backpressurestrategy/watermark%28low,high%29.md)
  A backpressure strategy using a high and low watermark to suspend and resume production respectively.
- [static func watermark(low: Int, high: Int, waterLevelForElement: (borrowing Element) -> Int) -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.BackpressureStrategy](./backpressurestrategy/watermark%28low,high,waterlevelforelement%29.md)
  A backpressure strategy using a high and low watermark to suspend and resume production respectively.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/backpressurestrategy)*