---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/makechannel(of:throwing:backpressurestrategy:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# makeChannel(of:throwing:backpressureStrategy:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Type Method

Initializes a new [`MultiProducerSingleConsumerAsyncChannel`](../multiproducersingleconsumerasyncchannel.md) and an [`MultiProducerSingleConsumerAsyncChannel.Source`](./source.md).

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func makeChannel(of elementType: Element.Type = Element.self, throwing failureType: Failure.Type = Never.self, backpressureStrategy: MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.BackpressureStrategy) -> sending MultiProducerSingleConsumerAsyncChannel<Element, Failure>.ChannelAndStream
```

#### Return Value

A struct containing the channel and its source. The source should be passed to the producer while the channel should be passed to the consumer.

## Parameters

- `elementType`: The element type of the channel.
- `failureType`: The failure type of the channel.
- `backpressureStrategy`: The backpressure strategy that the channel should use.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/makechannel(of:throwing:backpressurestrategy:))*