---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannel.Source.SendResult

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: enum  
**Role**: Enumeration

A type that indicates the result of sending elements to the source.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum SendResult
```

## Topics

### Structures
- [MultiProducerSingleConsumerAsyncChannel.Source.SendResult.CallbackHandle](./sendresult/callbackhandle.md)
  A handle that is returned when the channel’s backpressure strategy indicated that production should be suspended. Use this handle to enqueue a callback by  calling the [`enqueueCallback(onProduceMore:)`](./sendresult/callbackhandle/enqueuecallback%28onproducemore%29.md) method.
### Enumeration Cases
- [case enqueueCallback(MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.SendResult.CallbackHandle)](./sendresult/enqueuecallback%28_%29.md)
  Indicates that a callback should be enqueued.
- [MultiProducerSingleConsumerAsyncChannel.Source.SendResult.produceMore](./sendresult/producemore.md)
  Indicates that more elements should be produced and send to the source.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult)*