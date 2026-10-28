---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannelalreadyfinishederror"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannelAlreadyFinishedError

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An error that is thrown from the various `send` methods of the [`MultiProducerSingleConsumerAsyncChannel.Source`](./multiproducersingleconsumerasyncchannel/source.md).

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MultiProducerSingleConsumerAsyncChannelAlreadyFinishedError
```

## Overview

This error is thrown when the channel is already finished when trying to send new elements to the source.

## Relationships

### Conforms To
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannelalreadyfinishederror)*