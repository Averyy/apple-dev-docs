---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannel.Source

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A struct to send values to the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Source
```

Available when `Failure` conforms to `Error`.

## Overview

Use this source to provide elements to the channel by calling one of the `send` methods.

## Topics

### Structures
- [MultiProducerSingleConsumerAsyncChannel.Source.BackpressureStrategy](./source/backpressurestrategy.md)
  A struct representing the backpressure of the channel.
### Instance Methods
- [func finish(throwing: Failure?)](./source/finish%28throwing%29.md)
  Indicates that the production terminated.
- [func makeAdditionalSource() -> sending MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source](./source/makeadditionalsource%28%29.md)
  Creates a new source which can be used to send elements to the channel concurrently.
- [func send(consuming sending Element) async throws](./source/send%28_%29-5rwh7.md)
  Send new element to the channel.
- [func send(consuming sending Element) throws -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.SendResult](./source/send%28_%29-8ar29.md)
  Send the element to the channel.
- [func send(consuming sending Element, onProduceMore: (Result<Void, any Error>) -> Void)](./source/send%28_,onproducemore%29.md)
  Sends the element to the channel.
- [func send<S>(contentsOf: consuming sending S) async throws](./source/send%28contentsof%29-1h7t9.md)
  Send new elements to the channel.
- [func send<S>(contentsOf: consuming sending S) throws -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.SendResult](./source/send%28contentsof%29-3baoz.md)
  Sends new elements to the channel.
- [func send<S>(contentsOf: consuming sending S) async throws](./source/send%28contentsof%29-8cw3l.md)
  Send the elements of the asynchronous sequence to the channel.
- [func send<S>(contentsOf: consuming sending S, onProduceMore: (Result<Void, any Error>) -> Void)](./source/send%28contentsof,onproducemore%29.md)
  Send new elements to the channel and provide a callback which will be invoked once more elements should be produced.
- [func setOnTerminationCallback((() -> Void)?)](./source/setonterminationcallback%28_%29.md)
  Sets a callback to invoke when the channel terminated.
### Enumerations
- [MultiProducerSingleConsumerAsyncChannel.Source.SendResult](./source/sendresult.md)
  A type that indicates the result of sending elements to the source.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source)*