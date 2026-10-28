---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/channelandstream"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannel.ChannelAndStream

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A struct containing the initialized channel and source.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct ChannelAndStream
```

## Overview

This struct can be deconstructed by consuming the individual components from it.

```swift
var channelAndSource = MultiProducerSingleConsumerAsyncChannel.makeChannel(
    of: Int.self,
    backpressureStrategy: .watermark(low: 5, high: 10)
)
var channel = channelAndSource.takeChannel()
var source = consume channelAndSource.source
```

## Topics

### Instance Properties
- [var source: MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source](./channelandstream/source.md)
  The source.
### Instance Methods
- [func takeChannel() -> sending MultiProducerSingleConsumerAsyncChannel<Element, Failure>](./channelandstream/takechannel%28%29.md)
  Takes and returns the channel.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/channelandstream)*